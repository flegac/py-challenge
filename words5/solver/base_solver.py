from abc import ABC, abstractmethod
from pprint import pprint
from typing import Generator, Any

from solver.common.anagrams import Anagrams
from solver.common.utils import timing
from solver.common.words import Words


class BaseSolver(ABC):
    @abstractmethod
    def solve(self, words: Words) -> Generator[list[str], Any, None]:
        ...

    def run(self, words: Words, max_solutions: int = 5):
        with timing(f'solve({max_solutions})'):
            anagrams = Anagrams(words.words)
            classes = Words(anagrams.get_classes())
            pprint(f'{len(words)} words -> {len(classes)} classes')
            for idx, solution in enumerate(self.solve(classes)):
                if idx == max_solutions:
                    break
                pprint(_format(anagrams, solution))


def _format(anagrams: Anagrams, solution: list[str]):
    def _translate(item: list[str]):
        if len(item) == 1:
            return list(item)[0]
        return item

    return [
        _translate(_)
        for _ in list(map(anagrams.anagrams, sorted(solution)))
    ]
