
# https://leetcode.com/problems/maximum-number-of-words-you-can-type/?envType=problem-list-v2&envId=string
# Solved in: 5 m 27 sec - 8/14/2025
# Runtime: 0 ms - beats 100%
# Memory: 17.80 mb - beats 84.71%


class Solution:
    
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        #words = text.split()

        #result = [i for i in words if not any(True for x in brokenLetters if x in i)]

        #return len(result)"""

        count = 0

        for i in text.split():

            if any(True for x in brokenLetters if x in i):
                continue
            else:
                count += 1
        
        return count


it = Solution()
result = it.canBeTypedWords("hello world", "ad")
print(result)

