
# Solved in: 4 m 20 sec
# 5/21/2025
# Runtime: 335 ms - beats 5%
# Memory: 18.34 mb - beats 25.38%


class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        return len([i for i in set(words1 + words2) if i in set(words1 + words2) and words1.count(i) == 1 and words2.count(i) == 1])


it = Solution()
result = it.countWords(["leetcode","is","amazing","as","is"], ["amazing","leetcode","is"])
print(result)
