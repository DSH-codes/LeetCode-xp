

# Solved in: 4 m 24 sec
# 5/21/2025
# Runtime: 0 ms - beats 100%
# Memory: 17.81 - beats 29.99%


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return "".join([i.capitalize() + " " if len(i) > 2 else i.lower() + " " for i in title.split()]).strip()



it = Solution()
result = it.capitalizeTitle("capiTalIze tHe titLe")
print(result)
