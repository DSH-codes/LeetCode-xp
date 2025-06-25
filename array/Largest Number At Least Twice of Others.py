 
# https://leetcode.com/problems/largest-number-at-least-twice-of-others/?envType=problem-list-v2&envId=array
# Solved in: 29 minutes 
# 6/25/2025
# Runtime: 0 ms - beats 100%
# Memory: 17.67 mb - beats 78.91% 




class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        
        lr = nums[0]  # the largest
        ind = 0  # the index 
        
        for i in nums:  # manually find the largest without using Max 
            if i > lr:
                lr = i

        
        for i in nums: # manually track the index without using list.index
            if i == lr:
                break
            ind += 1
        
        for i in nums:
            
            if i == lr:
                continue
            if (i*2) > lr:
                return -1
        
        return ind



it = Solution()
result = it.dominantIndex([3,6,1,0])
print(result)

