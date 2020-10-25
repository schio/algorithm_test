# https://programmers.co.kr/learn/courses/30/lessons/12922
def solution(n):
    from itertools import cycle
    chars = cycle(["수", "박"])
    return "".join([item[1] for item in zip(range(n), chars)])
