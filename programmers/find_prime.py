# https://programmers.co.kr/learn/courses/30/lessons/12921
def solution(n):
    if n <= 2:
        return 1
    elif n == 3:
        return 2

    def find_prime(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    answer = 1
    for num in range(3, n + 1, 2):
        answer += 1 if find_prime(num) else 0
    return answer
