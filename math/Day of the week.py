
# Solved 3/28/2025 
# Time taken: 23 minutes

import calendar as cd 

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day = cd.weekday(year, month, day)
        return days[day]



it = Solution()
result = it.dayOfTheWeek(15,8,1993)
print(result)
