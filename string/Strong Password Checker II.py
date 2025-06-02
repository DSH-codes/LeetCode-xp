
# https://leetcode.com/problems/strong-password-checker-ii/submissions/1652147494/?envType=problem-list-v2&envId=string
# Solved in: 19 m 40 sec
# 6/3/2025
# Runtime: 3 ms - beats 16.15% 
# Memory: 17.68 mb - beats 82.13%

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        

    
        if len(password) < 8:
            return False

        if not [i for i in password if i.islower()]:
            return False
        
        if not [i for i in password if i.isupper()]:
            return False
        
        if not [i for i in password if i.isdigit()]:
            return False
        
        if not [i for i in password if i in "!@#$%^&*()-+"]:
            return False
        
        doubles = [i * 2 for i in set(password)] 

        for i in doubles:

            if i in password:
                return False
        
        return True


it = Solution()
result = it.strongPasswordCheckerII("yvTY#@IB#*!hjrQt-TLW&z)$@!%Duqt&ToskxHgnybqpndMI+wP&fcemIk#@KnkMTaUkcIbncpTL")

print(result)
