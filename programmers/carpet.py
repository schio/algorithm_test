# https://programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    for y in range(1, yellow + 1):
        if yellow % y == 0:
            x = yellow / y
            if brown == (x + 2) * (y + 2) - x * y:
                return [x + 2, y + 2]
