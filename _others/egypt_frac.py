"""

4/n = 1/A + 1/B + 1/C


n = 4ABC/(AB+BC+CA)

Let A=a.x, B=b.x, C=c.x,

n = [4abc/(ab+bc+ca)].x

prod = 44abc
sigma = (ab+bc+ca)

"""

from fractions import Fraction


class EgyFrac:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

        self.abc = a * b * c
        self.sigma = a * b + b * c + c * a

        self.fraction = Fraction(4 * self.abc, self.sigma)

    def __repr__(self):
        return f'[{self.a},{self.b},{self.c}] : {self.fraction}'


def find_frac(p: int, limit: int = 1000):
    for i in range(1, limit):
        frac = EgyFrac(2 * i * p, 2 * i, 1)
        if frac.fraction.numerator == 1:
            return frac


def main():
    # for p in primerange(2, 250):
    #     frac = find_frac(p)
    #     print(f'{p:2} : {frac}')

    print(find_frac(73, 20_000_000))
    print(find_frac(193, 20_000_000))


if __name__ == '__main__':
    main()
