# https://programmers.co.kr/learn/courses/30/lessons/42839#
from itertools import permutations


def solution(numbers):
    # 경우의 수 구성
    nums = list(numbers)
    for i in range(2, len(numbers) + 1):
        pm = permutations(numbers, i)
        for j in pm:
            if len(numbers) >= len(j):
                nums.append(''.join(j))
    nums = list(set([int(x) for x in nums]))

    # 예외 처리
    if nums == [0] or nums == [0, 1]:
        return 0
    for i in range(2):
        if nums.count(i):
            nums.remove(i)

    # 소수 판별
    answer = 0
    for num in nums:
        checker = True
        for i in range(2, num):
            if num % i == 0:
                checker = False
                break
        if checker:
            answer += 1
    return answer
