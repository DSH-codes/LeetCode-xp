# Solved in: 5 m 34 sec
# 5/20/2025
# Runtime: 9 ms - beats 42.32%
# Memory: 18.58 mb - beats 59.55%



class Solution:
    def countBits(self, n: int) -> list[int]:
        
        # I will check how to do it manually, using bitwise operators
        # For i while, enjoy this solution! 

        return [bin(i).count("1") for i in range(n + 1)]



it = Solution()
result = it.countBits(2)
print(result)
