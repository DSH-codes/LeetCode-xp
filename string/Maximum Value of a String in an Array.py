
# Solved in: 5 m 23 sec
# 5/21/2025
# Runtime: 0 ms - beats 100%
# Memory: 17.65 mb - beats 82.09% 


class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        
        return max([int(i) if i.isdigit() else len(i) for i in strs])




it = Solution()
result = it.maximumValue(["alic3","bob","3","4","00000"])
print(result)
