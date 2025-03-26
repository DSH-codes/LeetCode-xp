
# SOLVED 3/26/2025
# Time taken: 16:21 

import sys 

sys.set_int_max_str_digits(5000)    # to allow large digits conversion 


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = str(eval(f"{num1}+{num2}"))
        return result 



it = Solution()
result = it.addStrings("11", "123")
print(result)