from contextlib import contextmanager
from time import time

import numpy as np

LETTER_NUMBER = 26


@contextmanager
def timing(msg: str):
    start = time()
    try:
        yield
    finally:
        duration = time() - start
        print(f'{msg}: {duration:.3f}s')


def normalize(histogram: np.ndarray):
    hist = histogram - histogram.min()
    limit = hist.max()
    if limit != 0:
        hist = hist / limit
    return hist


def char_to_int(c: str):
    return ord(c) - ord('a')


def int_to_char(i: int):
    return chr(ord('a') + i)
