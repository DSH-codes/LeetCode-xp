

# SOLVED 3/16/2025 6:44 AM
# Time taken = 16 minutes 

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        nums[:] = [i for i in nums if i] + [i for i in nums if not i]
        

x = [0,1,0,3,12]
it = Solution()
it.moveZeroes(x)
print(x)