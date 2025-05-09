
# Solved in: 18m  45 sec
# 5/10/2025
# Runtime: 3ms - beats 95.48% 
# Memory: 17.81 mb - beats 80.09% 


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(set(t)) != len(set(s)):
            return False
        
        map_ = {k:v for k,v in zip(s, t)}

        for i in range(len(s)):

            if map_[s[i]] != t[i]:
                return False
                
        return True
        




it = Solution()
print(it.isIsomorphic("badc", "baba"))
