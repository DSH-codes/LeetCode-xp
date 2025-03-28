
# Solved 3/28/2025
# Time taken: 4 minutes 


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return [i for i in nums if nums.count(i) == 1][0]


it = Solution()
result = it.singleNumber([8,1,1,4,4])
print(result)
