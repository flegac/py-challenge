from pathlib import Path
from typing import Iterable

import numpy as np

from solver.common.utils import char_to_int, LETTER_NUMBER


class Words:
    @staticmethod
    def from_path(path: Path):
        with path.open() as _:
            words = _.read().splitlines()
        return Words(words)

    def __init__(self, words: Iterable[str], word_length: int = 5):
        self.word_length = word_length
        self.words = self.prepare(words, word_length)
        self._stats = None

    def __len__(self):
        return len(self.words)

    def __iter__(self):
        for _ in self.words:
            yield _

    @property
    def stats(self):
        if self._stats is None:
            stats = np.zeros(LETTER_NUMBER)
            for word in self.words:
                for letter in word:
                    index = char_to_int(letter)
                    stats[index] += 1
            stats /= stats.sum()
            self._stats = stats
        return self._stats

    @staticmethod
    def prepare(words: Iterable[str], word_length: int):
        words = map(str.lower, words)
        words = filter(lambda _: "'" not in _, words)
        words = filter(lambda _: len(_) == word_length, words)
        words = filter(lambda _: len(set(_)) == word_length, words)
        return list(words)
