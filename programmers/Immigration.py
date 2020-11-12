# https://programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    left, right = 1, max(times) * n
    min_time = 0
    while left <= right:
        mid = (left + right) // 2
        print(mid, 10 // 2)
        th = n
        for i in times:
            th -= mid // i
            if th <= 0:
                min_time = mid
                right = mid - 1
                break
        if th > 0:
            left = mid + 1
    return min_time
