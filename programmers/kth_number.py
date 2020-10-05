"""
https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3
"""


def solution(array, commands):
    answer = []
    for start, end, mid in commands:
        answer.append(sorted(array[start - 1:end])[mid - 1])
    return answer
