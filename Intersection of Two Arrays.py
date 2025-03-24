
# SOLVED 3/16/2025
# Time taken = 8:43 minutes 

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        elems = set(nums1) & set(nums2)
        return list(elems)



it = Solution()
result = it.intersection([4,9,5], [9,4,9,8,4])
print(result)