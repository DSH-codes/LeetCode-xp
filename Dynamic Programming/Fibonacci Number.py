

# Solved in: 3 m 47 sec 
# 5/20/2025
# Runtime: 334 ms - beats 26.25%
# Memory: 17.63 mb - beats 64.34% 

class Solution:
    def fib(self, n: int) -> int:
        
        if n <= 1:
            return n
        
        return self.fib(n-1) + self.fib(n - 2)


it = Solution()
result = it.fib(11)

print(result)
