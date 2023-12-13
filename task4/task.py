from math import log2
from typing import List, Tuple


def entropy(mas):
    summa = 0
    for i in mas:
        if i > 0:
            summa += i * log2(i)
    return -summa


def counting(k):
    summas = {i: 0 for i in range(2, 13)}
    multiplies = {i: 0 for i in range(1, 37)}
    comb = {}

    for i in range(1, 7):
        for j in range(1, 7):
            summas[i + j] += 1
            multiplies[i * j] += 1
            comb[(i + j, i * j)] = comb.get((i + j, i * j), 0) + 1

    summas = [i / k for i in summas.values()]
    multiplies = [i / k for i in multiplies.values()]
    comb = [i / k for i in comb.values()]

    return summas, multiplies, comb


def task() -> list[float]:
    combinations = 36

    summas, multiplies, comb = counting(combinations)

    summas = round(entropy(summas), 2)
    multiplies = round(entropy(multiplies), 2)
    comb = round(entropy(comb),2)
    usl = round(comb - summas, 2)
    inf = round(multiplies - usl, 2)

    return [comb, summas, multiplies, usl, inf]


print(task())