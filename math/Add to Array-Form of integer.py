



class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        return [int(i) for i in str(int(''.join([str(i) for i in num])) + k)]




it = Solution()
result = it.addToArrayForm([2,7,4], 181)
print(result)
