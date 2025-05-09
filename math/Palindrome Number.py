
# Solved in: 5:18 sec. 
# 5/6/2025 1:13 AM 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0: 
            return False

        if str(x) == str(x)[::-1]:
            return True
        
        return False 
    


it = Solution()

print(it.isPalindrome(321))
