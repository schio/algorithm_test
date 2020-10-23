# https://programmers.co.kr/learn/courses/30/lessons/12912
def solution(a, b):
    if a > b:
        a, b = b, a
    return sum(num for num in range(a, b + 1))
