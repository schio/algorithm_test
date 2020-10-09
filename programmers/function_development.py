# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    import collections
    progresses = collections.deque(progresses)
    speeds = collections.deque(speeds)
    deploy_counts = []
    while progresses:
        # 100 이상인 것들 카운트
        deploy_count = 0
        pop_cnt = 0
        for i in range(len(progresses)):
            i -= pop_cnt
            if progresses[i] >= 100:
                deploy_count += 1
                speeds.popleft()
                progresses.popleft()
                pop_cnt += 1
            else:
                break

        # count 만큼 pop
        if deploy_count:
            deploy_counts.append(deploy_count)

        for i in range(len(progresses)):
            progresses[i] += speeds[i]

    return deploy_counts
