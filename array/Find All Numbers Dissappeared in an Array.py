# Solved in: 42 m 24 sec
# Runtime: 21 ms - beats 82.18%
# Memory: 31.49 mb - beats 53.89% 



class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        
        s = set(nums)
        back = []
        for i in range(len(nums) + 1):
            if i not in s and i > 0:
                back.append(i)

        return back




it = Solution()
result = it.findDisappearedNumbers([1,1]) 
print(result)  
