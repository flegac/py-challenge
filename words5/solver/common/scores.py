from abc import ABC, abstractmethod

from solver.common.utils import char_to_int
from solver.common.word_filter import WithoutLettersFilter
from solver.common.words import Words


class WScore(ABC):
    def __init__(self, words: Words):
        self.words = words

    @abstractmethod
    def score(self, word: str) -> float:
        ...

    def __call__(self, word: str):
        return self.score(word)

    def sorted(self, words: Words):
        return Words(sorted(words.words, key=self.score))


class SquareScore(WScore):
    def score(self, word: str):
        return sum([pow(self.words.stats[char_to_int(_)], 2) for _ in word]) / len(word)


class CustomScore(WScore):
    def score(self, word: str):
        return sum([pow(1 - self.words.stats[char_to_int(_)], 4) for _ in word]) / len(word)


class ConnectionScore(WScore):
    def score(self, word: str) -> float:
        return len(list(filter(WithoutLettersFilter(word), self.words)))
