
# https://leetcode.com/problems/find-closest-number-to-zero/
# Solved in: 22 m 39 sec
# 5/26/2025
# Runtime: 0 ms - beats 100%
# Memory: 17.83 mb - beats 74.52%


class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        
        mn = min(nums)
        mx = max(nums)


        for i in nums:
            
            if i == 0:  # if it is 0, return it right away
                return 0
            
            if i != 0 and i > mn and i < 0:    # < - we do not need to check that it is not equal to zero, because we check it above, and return it, but when this checking if placed there, the runtime is 0 ms, when you remove it, it is 3 ms, for unknown reason :(
                mn = i

            elif i < mx and i > 0:
                mx = i

        return mn if abs(mn) < mx else mx  # to return -1321, in case of -1321 and 1762 

        

it = Solution()
result = it.findClosestNumber([-4,-2,1,4,8])
print(result)

