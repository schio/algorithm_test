# https://programmers.co.kr/learn/courses/30/lessons/42583
def solution(bridge_length, weight, truck_weights):
    from collections import deque as q
    second = 0
    queue = [0] * bridge_length

    while queue:
        second += 1
        del queue[0]

        if truck_weights:
            queue.append(truck_weights.pop(0) if truck_weights[0] + sum(queue) <= weight else 0)

    return second
