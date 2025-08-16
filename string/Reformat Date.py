



# https://leetcode.com/problems/reformat-date/?envType=problem-list-v2&envId=string
# Solved in: 23 m 40 sec
# 6/2/2025
# Runtime: 0 ms - beats 100%
# Memory: 17.55 mb - beats 97.40%


class Solution:
    def reformatDate(self, date: str) -> str:
        
        months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
        
        sdate = date.split()

        day = "".join([i for i in sdate[0] if i.isdigit()])
        day = day if len(day) == 2 else "0" + day
        
        month = months.index(sdate[1]) + 1
        month = month if len(str(month)) == 2 else "0" + str(month)

        return f"{sdate[2]}-{month}-{day}"



it = Solution()
result = it.reformatDate("20th Oct 2052")
print(result)
