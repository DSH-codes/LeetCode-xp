# https://leetcode.com/problems/sorting-the-sentence/?envType=problem-list-v2&envId=sorting
# Solved in: 14 m 33 sec
# 5/27/2025
# Runtime: 41 ms - beats 30.83%
# Memory: 17.92 mb - beats 28.30% 



class Solution:

    def sortSentence(self, s: str) -> str:
        
        res = "123456789"[:s.count(" ") + 1] # cut off the digits we do not need 


        for i in s.split():
            res = res.replace(i[-1], " " + i[:-1])   # replace every digit, by a corresponding word, cutting off the trailing digit 
        
        return res.strip() # cut off possible trailing empty space 



it = Solution()
result = it.sortSentence("is2 sentence4 This1 a3")
print(result)
