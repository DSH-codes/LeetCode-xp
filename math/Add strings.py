


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = eval(f"hex({num1}) + hex({num2})")
        result = str(result)
        return eval("int({result}, 16)")



it = Solution()
result = it.addStrings("11", "123")
print(result)