# https://programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    from itertools import combinations
    return sorted(set([sum(nums) for nums in combinations(numbers, 2)]))
