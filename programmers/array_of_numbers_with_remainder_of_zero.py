# https://programmers.co.kr/learn/courses/30/lessons/12910
def solution(arr, divisor):
    answer = [num for num in arr if num % divisor == 0]
    if answer:
        return sorted(answer)
    else:
        return [-1]
