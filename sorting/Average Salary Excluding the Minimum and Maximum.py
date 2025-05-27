
# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/?envType=problem-list-v2&envId=sorting
# Solved in: 7 m 43 sec
# Runtime: 0 ms - beats 100%
# Memory: 18.05 ms - beats 24.63%
# 5/27/2025



class Solution:
    def average(self, salary: list[int]) -> float:
        
        # are max and min allowed to be used? I do not know, so let's do it mannually 


        mn = salary[0]
        mx = salary[0]
        
        for i in salary:
            if i < mn:
                mn = i
        
        for i in salary:
            if i > mx:
                mx = i

        salary.remove(mn)
        salary.remove(mx)

        mx = 0
        ln = 0

        for i in salary:
            mx += i
            ln += 1

        return mx / ln


it = Solution()
result = it.average([4000,3000,1000,2000])
print(result)
