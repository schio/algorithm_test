# https://programmers.co.kr/learn/courses/30/lessons/70128def solution(a, b):
def solution(a, b):
    return sum([num1 * num2 for num1, num2 in zip(a, b)])
