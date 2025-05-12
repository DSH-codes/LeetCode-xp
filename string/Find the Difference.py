# Solved in: 10 m 25 sec
# 5/13/2025
# Runtime: 3ms - beats 55.37%
# Memory: 17.79mb - beats 68.88% 


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        # can't do it by sets, you have to take them out one by one
        
        for i in s:
            t = t.replace(i, "", 1)
        
        return t


it = Solution()
result = it.findTheDifference("abcd", "abcde")
print(result)


