# https://programmers.co.kr/learn/courses/30/lessons/12932
def solution(n):
    return list(map(int, list(str(n))[::-1]))
