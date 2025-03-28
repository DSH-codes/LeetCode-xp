
# Solved 3/28/2025
# Time taken: 4 minutes 


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return [i for i in nums if nums.count(i) == 1][0]


it = Solution()
result = it.singleNumber([4,1,2,1,2])
print(result)
