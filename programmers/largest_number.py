"""
https://programmers.co.kr/learn/courses/30/lessons/42746
"""
import functools


def solution(numbers):
    def comparator(n1, n2):
        number_1 = int(n1 + n2)
        number_2 = int(n2 + n1)

        return (number_1 > number_2) - (number_1 < number_2)

    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=functools.cmp_to_key(comparator), reverse=True)

    answer = str(int("".join(numbers)))
    return answer
