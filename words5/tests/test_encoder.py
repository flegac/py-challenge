from unittest import TestCase

from solver.common.encoder import Encoder


class TestEncoder(TestCase):
    def test_encoder(self):
        words = ['ajhfbdslq', 'besztgfdesq', 'cvdsqdfa', 'vcaqpdigur', 'nytrtrezscaqsdfsq']
        algo = Encoder()

        canonical_words = list(map(algo.canonical, words))
        encoded = list(map(algo.encode, canonical_words))
        decoded = list(map(algo.decode, encoded))

        self.assertEqual(decoded, canonical_words)
