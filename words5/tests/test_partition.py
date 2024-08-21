from pathlib import Path
from unittest import TestCase

from solver.common.partition import Partition
from solver.common.words import Words


class TestPartition(TestCase):
    def test_partition(self):
        words = Words.from_path(Path.cwd() / 'resources/words.txt')
        algo = Partition()

        parts = algo.partition(level=5, words=words.words)

        print(list(map(len, parts)))
