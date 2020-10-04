"""
https://programmers.co.kr/learn/courses/30/lessons/42578
"""
from collections import defaultdict
from functools import reduce

from operator import mul
def solution(clothes):
    category = defaultdict(lambda: 1)
    for c in clothes:
        category[c[1]] += 1

    return reduce(mul, category.values()) - 1