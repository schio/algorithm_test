# https://programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities, location):
    answer = 0

    from collections import deque
    queue = deque([(doc, idx) for idx, doc in enumerate(priorities)])

    while len(queue):
        doc, idx = queue.popleft()
        if queue and max(queue)[0] > doc:
            queue.append((doc, idx))
        else:
            answer += 1
            if idx == location:
                break
    return answer
