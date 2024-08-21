from abc import ABC, abstractmethod
from typing import Callable

from solver.common.words import Words


class WFilter(ABC, Callable[[str], bool]):
    @abstractmethod
    def accept(self, word: str) -> bool:
        ...

    def __call__(self, word: str):
        return self.accept(word)

    def apply(self, words: Words):
        return Words(filter(self, words.words))


class WordFilter(WFilter):
    def __init__(self, excluded: str):
        self.excluded = set(excluded)

    def accept(self, word: str):
        return self.excluded.isdisjoint(word)


class WithLettersFilter(WFilter):
    def __init__(self, letters: str):
        self.letters = set(letters)

    def accept(self, word: str):
        return not self.letters.isdisjoint(word)


class WithoutLettersFilter(WFilter):
    def __init__(self, letters: str):
        self.letters = set(letters)

    def accept(self, word: str):
        return self.letters.isdisjoint(word)
