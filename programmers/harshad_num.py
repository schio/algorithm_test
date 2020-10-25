# https://programmers.co.kr/learn/courses/30/lessons/12947
def solution(x):
    nums = [int(s) for s in str(x)]
    return (x % sum(nums)) == 0
