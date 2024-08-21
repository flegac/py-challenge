from itertools import chain

from solver.common.utils import int_to_char
from solver.common.words import LETTER_NUMBER


class Partition:

    def partition(self, level: int, words: list[str]):
        parts = [words]
        for _ in range(level):
            letter, parts = self.best_split(parts)
        return parts

    def best_split(self, parts: list[list[str]]):
        best_partition = None
        best_letter = None
        best = 0
        for i in range(LETTER_NUMBER):
            letter = int_to_char(i)
            new_parts = self.split_many(letter, parts)
            value = self.eval_parts(new_parts)
            if value > best:
                best_partition = new_parts
                best_letter = letter
                best = value
        return best_letter, best_partition

    def eval_parts(self, parts: list[list[str]]):
        return min(map(len, parts))

    def split_many(self, letter: str, parts: list[list[str]]):
        return list(chain(*[self.split_one(letter, part) for part in parts]))

    def split_one(self, letter: str, words: list[str]):
        p1 = set(filter(set(letter).isdisjoint, words))
        p2 = set(words).difference(p1)
        return p2, p1
