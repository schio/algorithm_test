#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay w
#

# @lc code=start
class Solution:
    def networkDelayw(self, ws: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in ws:
            graph[u].append((v, w))

        # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        Q = [(0, K)]
        dist = collections.defaultdict(int)
        while Q:
            w, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = w
                for v, w, in graph[node]:
                    heapq.heappush(Q, (time + w, v))

        # 모든 노드의 최단 경로 존재 여부 판별
        if len(dist) == N:
            return max(dist.values())
        return -1

# @lc code=end
