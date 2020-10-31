#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in flights:
            graph[u].append((v, w))

        queue = [(0, src, K)]  # (가격, 정점, 가능한 남은 경유지 수)

        while queue:
            price, node, k = heapq.heappop(queue)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    heapq.heappush(queue, (price + w, v, k - 1))
        return -1


# @lc code=end
