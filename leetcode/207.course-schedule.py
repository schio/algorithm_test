#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        # make graph
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()
        visited = set()

        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                return False

            # 이미 방문한 노드라면 True
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False

            # 탐색 종료, 순환 노드 삭제
            traced.remove(i)

            # 탐색 종료, 방문 노드 추가
            visited.add(i)

            return True

        for x in list(graph):
            if not dfs(x):
                return False
        return True


# @lc code=end
