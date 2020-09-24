#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Data in Log Files
#

# @lc code=start
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        lets, digs = [], []
        for log in logs:
            digs.append(log) if log.split()[1].isdigit() else lets.append(log)
                
        lets.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return lets + digs
# @lc code=end

