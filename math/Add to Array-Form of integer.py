
# Solved 3/28/2025
# Time taken: 10 minutes 

# import sys 
# sys.set_int_max_str_digits()
# increase max_str if you need 

class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        return [int(i) for i in str(int(''.join([str(i) for i in num])) + k)]




it = Solution()
result = it.addToArrayForm([2,7,4], 181)
print(result)
