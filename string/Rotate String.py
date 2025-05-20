

# Solved in: 6 m 26 sec
# 5/20/2025
# Runtime: 5 ms - beats 1.62%
# Memory: 17.61 mb - beats 80.08% 




class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        s = list(s)

        for i in range(len(s)):
            
            head = s[0]
            del s[0]
            s.append(head)
            
            if "".join(s) == goal:
                return True
        
        return False


it = Solution()
result = it.rotateString("abcde", "cdeab")
print(result)


# someone's genius solution 

# class Solution:
#     def rotateString(self, s: str, goal: str) -> bool:
#         return len(s) == len(goal) and s in goal+goal