
# Solved in: 5 m 39 sec
# 5/13/2025
# Runtime: 7ms - beats 93.15%
# Memory: 17.81 mb - beats 82.08% 

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        for i in set(ransomNote):

            if ransomNote.count(i) > magazine.count(i):

                return False

        return True




it = Solution()
result = it.canConstruct("aa", "aaa")

print(result)



