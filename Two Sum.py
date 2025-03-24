

# SOLVED 3/16/2025 4:10 AM 

# (27:42 time taken)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        twin = nums.copy()

        for i in nums:
            twin.remove(i)
            for x in twin:
                if i + x == target:
                    them = [nums.index(i)]
                    nums[nums.index(i)] = ["-"]
                    them.append(nums.index(x))
                    return them


it = Solution()
result = it.twoSum([3,3], 6)
print(result)