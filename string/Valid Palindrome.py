

# Solved in 18m 51 sec 
# 5/9/2025
# Runtime: 11ms - beats 36.12% 

import string as st


class Solution:
    def isPalindrome(self, s: str) -> bool:

        
        s = [i for i in s if i in st.ascii_letters+st.digits]
        s = "".join(s).lower()

        if s.isspace():
            return True

        if s == s[::-1]:
            return True

        return False 


it = Solution()

result = it.isPalindrome("0P")

print(result)
