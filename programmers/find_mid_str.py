# https://programmers.co.kr/learn/courses/30/lessons/12903
def solution(s):
    len_s = len(s)
    mid = int(len_s / 2)
    if len_s % 2 == 1:
        return s[mid]
    else:
        return s[mid - 1:mid + 1]
