 
# https://leetcode.com/problems/sort-the-people/submissions/1653039295/?envType=problem-list-v2&envId=string
# Solved in: 4 m 38 sec
# 6/3/2025
# Runtime: 3 ms - beats 81.07%
# Memory: 18.10 mb - beats 93.74%


class Solution:

    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        
        they = {v:k for k,v in zip(names, heights)}
        heights.sort()

        return [they[i] for i in heights][::-1]



it = Solution()
result = it.sortPeople(["Mary","John","Emma"], [180,165,170])
print(result)
