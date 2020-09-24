#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#

# @lc code=start
import re
import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r"[^\w]", " ", paragraph).lower().split() if word not in banned]

        cnt = collections.Counter(words)
        return cnt.most_common(1)[0][0]

# @lc code=end

