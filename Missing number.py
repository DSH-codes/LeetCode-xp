
# SOLVED 3/16/2025 6:24 AM
# Time taken = 6.52 minutes 

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for i in range(len(nums) + 1):
            if i not in nums:
                return i


it = Solution()
result = it.missingNumber([3,0,1])
print(result)