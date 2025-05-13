

# Solved in: 13 m 28 sec
# 05/13/2025
# Runtime: 15 ms - beats 73.05%
# Memory: 20.14 mb - beats 56.17% 


class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        
        co = 0 # outer counter 
        ci = 0 # inner counter 
        
        for i in nums: 
            
            if i:
                ci += 1
            else:
                co = ci if ci > co else co
                ci = 0

        co = ci if ci > co else co # move the last result to co before returning 

        return co 

it = Solution()
result = it.findMaxConsecutiveOnes([1,1,0,1,1,1,1,1,0,1,1,0,1,1,1])

print(result)
