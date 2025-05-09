
# Solved in: 4m 31 sec
# 5/10/2025
# Runtime: 0ms - beats 100.00%
# Memory: 17.65 mb - beats 79.89% 


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        
        #                          5    3    2                 1               4
        # return [int(x) for x in str(int("".join([str(i) for i in digits])) + 1)]
        
        # 1 - comprehension to convert all digits in string in the list
        # 2 - join them into one string
        # 3 - convert the string into an integer
        # 4 - increments the integers
        # 5 - convert the integer back into a string
        # then you just make a list out of a string by a comprehension 



        return [int(x) for x in str(int("".join([str(i) for i in digits])) + 1)]


it = Solution()
result = it.plusOne([5,7,1])
print(result)
