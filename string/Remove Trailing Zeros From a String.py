 

# Solved in two minutes; Feb 2 2026 

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip("0")


it = Solution()

result = it.removeTrailingZeros("51230100")
print(result)
