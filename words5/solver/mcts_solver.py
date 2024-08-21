import math
from typing import List, Generator, Any, Type

from solver.common.encoder import Encoder
from solver.common.scores import WScore
from solver.common.word_filter import WordFilter, WithoutLettersFilter
from solver.common.words import Words
from solver.base_solver import BaseSolver

Key = int
ENCODER = Encoder()


class Node:
    def __init__(self, word: str = None, key: Key = None):
        self.word = word or ''
        self.key = ENCODER.encode(self.word) if key is None else key
        self.tries = 0
        self.successes = 0
        self.children: List[Key] = None


class MCTSSolver(BaseSolver):
    ROOT_KEY = ENCODER.encode('')

    def __init__(self, score: Type[WScore]):
        self.score = score
        self.nodes: dict[Key, Node] = {
            MCTSSolver.ROOT_KEY: Node()
        }

    def try_solve(self, words: Words):
        current = MCTSSolver.ROOT_KEY
        solution = []
        solution_keys = [current]
        while True:
            try:
                found = self.select_next(current, words)
                link_word = self.link_word(current, found)
                solution.append(link_word)
                solution_keys.append(found)
                current = found
            except:
                break
        for key in solution_keys:
            node = self.nodes[key]
            node.tries += 1
            if len(solution) == 5:
                node.successes += 1

        return solution

    def link_word(self, parent_key: Key, child_key: Key):
        parent = self.nodes[parent_key]
        child = self.nodes[child_key]
        parent = ENCODER.decode(parent_key)
        child = ENCODER.decode(child_key)
        return ''.join(set(child).difference(parent))

    def select_next(self, key: Key, words: Words) -> Key:
        self.update_children(key, words)
        node = self.nodes[key]

        score_func = self.score(words)

        def score(child_key: Key):
            child = self.nodes[child_key]
            parent_tries = node.tries
            tries = child.tries
            successes = child.successes
            if tries == 0:
                tries = 1
            exploration_score = math.sqrt(2 * parent_tries / tries)
            win_score = successes / tries if tries != 0 else 0
            child_word = ENCODER.decode(child.key)
            base_score = score_func(child_word)
            mcts_score = win_score + exploration_score

            return base_score + mcts_score

        selected = max(node.children, key=score)
        return selected

    def update_children(self, key: Key, words: Words):
        parent_word = ENCODER.decode(key)
        filtered_words = WithoutLettersFilter(parent_word).apply(words)
        node = self.nodes[key]
        if node.children is None:
            node.children = []
            for word in filtered_words:
                child_word = ''.join([parent_word, word])
                child_key = ENCODER.encode(child_word)
                if child_key not in self.nodes:
                    self.nodes[child_key] = Node(word, child_key)
                node.children.append(child_key)

    def solve(self, words: Words) -> Generator[list[str], Any, None]:
        while True:
            solution = self.try_solve(words)
            if len(solution) >= 5:
                yield solution
