from collections import defaultdict


class Anagrams:
    def __init__(self, words: list[str]):
        self._classes = _compute_table(words)

    def anagrams(self, word: str):
        return self._classes[_key(word)]

    def get_classes(self):
        return list(self._classes.keys())


def _compute_table(words: list[str]):
    classes = defaultdict(set)
    for w in words:
        key = _key(w)
        classes[key].add(w)
    return dict(classes)


def _key(word: str):
    return ''.join(sorted(word))
