

# Solved in: 4 m 14 sec
# 5/21/2025
# Runtime: 0 ms - beats 100%
# Memory 17.77 mb - 91.37% 



class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        
        # return len([i for i in words if i.startswith(pref)]) - one liner! 


        count = 0

        for i in words:
            if i.startswith(pref):
                count += 1

        return count 




it = Solution()
out = it.prefixCount(["pay","attention","practice","attend"], "at")
print(out)
