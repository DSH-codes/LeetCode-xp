

# Solved in 29 minutes; Feb 9 2026 



class Solution:
    def largestEven(self, s: str) -> str:
        
        if s == "1":
            return ""
            
        for i in range(len(s)):

            if int(s) % 2 == 0:
                return s
            elif s.isspace():
                return s
            else:
                s = s[:-1]
            


it = Solution()
result = it.largestEven("1112")
print(result)
