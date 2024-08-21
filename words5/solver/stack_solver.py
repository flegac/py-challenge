from typing import Type

from solver.base_solver import BaseSolver
from solver.common.scores import SquareScore, WScore
from solver.common.word_filter import WithoutLettersFilter
from solver.common.words import Words


class StackItem:
    def __init__(self, words: Words, score: Type[WScore] = SquareScore):
        self.score = score
        score_func = score(words)
        self.word_scores = {
            word: score_func(word)
            for word in words.words
        }
        self.words = score_func.sorted(words)
        self.word = self.words.words[0]

    def iter_words(self):
        for self.word in self.words.words:
            yield self.word

    def get_next(self, word: str):
        compatible_words = WithoutLettersFilter(word).apply(self.words)
        if len(compatible_words) == 0:
            return None
        return StackItem(compatible_words, self.score)


class StackSolver(BaseSolver):
    def __init__(self, score: Type[WScore]):
        self.score = score
        self.stack: list[StackItem] = []

    def get_solution(self):
        return [item.word for item in self.stack]

    def is_solved(self):
        return len(self.stack) == 5

    @property
    def current(self):
        return self.stack[-1]

    def try_solve(self, current: StackItem):
        if self.is_solved():
            yield self.get_solution()

        for word in current.iter_words():
            item = current.get_next(word)
            if item is None or len(item.words) < 5 - len(self.stack):
                continue
            self.stack.append(item)
            for solution in self.try_solve(item):
                yield solution
            self.stack.pop()

    def solve(self, words: Words):
        self.stack.append(StackItem(words, self.score))

        for solution in self.try_solve(self.current):
            yield solution
        self.stack = []
