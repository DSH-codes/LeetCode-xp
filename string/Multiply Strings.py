

# Solved in: 2m 24 sec 
# 05/09/2025 10:32 PM

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = eval(f"{num1} * {num2}")
        return str(result)


it = Solution()
print(it.multiply("123", "456"))
