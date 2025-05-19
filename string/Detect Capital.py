
# Solved in: 5 m 15 sec
# 05/20/2025
# Runtime: 0 ms - beats 100% 
# Memory: 17.67 - beats 75.93% 

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if word.capitalize() == word:
            return True
        
        if word.upper() == word:
            return True

        if word.islower():
            return False 
        
        return False 




it = Solution()
result = it.detectCapitalUse("s")

print(result)
