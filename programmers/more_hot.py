# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq


def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while True:
        if len(scoville) <= 1 and scoville[0] < K:
            cnt = -1
            return cnt
        elif scoville[0] >= K:
            return cnt
        else:
            new_scoville = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
            heapq.heappush(scoville, new_scoville)
            cnt += 1
