from pathlib import Path
from unittest import TestCase

from solver.common.anagrams import Anagrams
from solver.common.utils import int_to_char
from solver.common.word_filter import WithLettersFilter
from solver.common.words import Words

words = Words.from_path(Path.cwd() / 'resources/words.txt')
anagrams = Anagrams(words)
classes = Words(anagrams.get_classes())


class ComputeStats(TestCase):
    def test_letter_stats(self):
        stats = {
            int_to_char(idx): v
            for idx, v in enumerate(classes.stats)
        }
        # for k in sorted(stats, key=stats.get):
        #     print(f'{k}: {stats[k]}')

        # for k in sorted(stats, key=stats.get):
        #     selection = WithLettersFilter(k).apply(classes)
        #     print(f'{k}: {sorted(selection.stats)}')
        for idx, k in enumerate(sorted(stats, key=stats.get)):
            selection = WithLettersFilter(k).apply(classes)
            print(f'{k}: {len(selection)} : {selection.words[:10]}')
