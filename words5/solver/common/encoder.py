from solver.common.utils import char_to_int, int_to_char
from solver.common.words import LETTER_NUMBER


class Encoder:
    def canonical(self, word: str):
        return self.decode(self.encode(word))

    def encode(self, word: str):
        assert len(word) <= LETTER_NUMBER
        letters = list(map(char_to_int, set(word)))
        return sum(2 ** _ for _ in letters)

    def decode(self, value: int):
        letters = []
        for i in range(LETTER_NUMBER):
            if (value >> i) & 1:
                letters.append(int_to_char(i))
        return ''.join(sorted(letters))
