 
# https://leetcode.com/problems/sort-array-by-parity/?envType=problem-list-v2&envId=array
# Solved in: 4 m 38 sec
# 6/29/2025
# Runtime: 0 ms - beats 100%
# Memory: 18.71 mb - beats 14.84% 




class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:

        return [i for i in nums if i % 2 == 0] + [i for i in nums if i % 2]

        



it = Solution()
result = it.sortArrayByParity([3,1,2,4])
print(result)