
# SOLVED 3/16/2025 6:00 AM 
# Time taken = 5 minutes 

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return True if len(set(nums)) != len(nums) else False 



it = Solution()
result = it.containsDuplicate([1,2,3,4,4])
print(result)