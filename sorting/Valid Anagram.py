
# SOLVED 3/25/2025  
# Time: 15 mimutes 


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True


it = Solution()
print(it.isAnagram("anagram", "nagaram"))
