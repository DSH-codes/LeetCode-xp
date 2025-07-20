
# https://leetcode.com/problems/jewels-and-stones/submissions/1704659753/?envType=problem-list-v2&envId=string
# Solved in: 2 m 40 sec 
# Date: 7/20/2025
# Runtime: 0 ms - beats 100%
# Memory: 17.94 mb - beats 10.47% 



class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        return len([i for i in stones if i in jewels])




it = Solution()
result = it.numJewelsInStones("aA", "aAAbbbb")
print(result)



