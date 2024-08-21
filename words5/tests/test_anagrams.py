from unittest import TestCase

from solver.common.anagrams import Anagrams


class TestAnagrams(TestCase):
    def test_anagrams(self):
        words = ['abcd', 'bacd', 'badc', 'efgh', 'fegh']
        anagrams = Anagrams(words)

        self.assertEqual(set(anagrams.anagrams('abcd')), {'abcd', 'bacd', 'badc'})
        self.assertEqual(set(anagrams.anagrams('efgh')), {'efgh', 'fegh'})
        self.assertEqual(len(anagrams.get_classes()), 2)


