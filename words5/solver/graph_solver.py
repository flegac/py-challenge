import networkx as nx
from networkx import find_cliques

from solver.base_solver import BaseSolver
from solver.common.partition import Partition
from solver.common.utils import timing
from solver.common.words import Words


class Node:
    def __init__(self, words: Words):
        self.words = words
        self.children: list[Node] = None
        self.split_char = self.find_split_char()

    def find_split_char(self):
        stats = self.words.stats
        total = self.size()
        best_idx = -1
        best_val = 1.
        for idx, count in enumerate(stats):
            val = abs(.5 - count / total)
            if val < best_val:
                best_idx = idx
                best_val = val

        return chr(ord('a') + best_idx)

    def expand(self, depth: int):
        if depth == 0:
            return
        self.split()
        for node in self.children:
            node.expand(depth - 1)

    def split(self):
        if self.children is not None:
            return
        p1 = set(filter(set(self.split_char).isdisjoint, self.words))
        p2 = set(self.words).difference(p1)
        assert len(self.words) == len(p1) + len(p2)
        self.children = [Node(Words(p1)), Node(Words(p2))]

    def __repr__(self):
        if self.children is None:
            return f'{self.size()}'
        return f'{self.split_char}{self.children}'

    def size(self):
        return len(self.words)


def add_edges(graph, p1: list[str], p2: list[str]):
    # with timing(f'graph add_edges({len(p1), len(p2)})'):
    edges = []
    for w1 in p1:
        for w2 in p2:
            if set(w1).isdisjoint(w2):
                edges.append((w1, w2))
    graph.add_edges_from(edges)


class GraphSolver(BaseSolver):
    def solve(self, words: Words):
        tree = Node(words)
        tree.expand(depth=2)

        parts = Partition().partition(level=4, words=words.words)
        left = parts[: len(parts) // 2]
        right = parts[len(parts) // 2:]

        graph = nx.Graph()
        with timing(f'graph creation({len(words)})'):
            for p1, p2 in zip(left, reversed(right)):
                add_edges(graph, p1, p2)

        with timing(f'max_clique'):
            for solution in find_cliques(graph):
                if len(solution) == 5:
                    yield solution
