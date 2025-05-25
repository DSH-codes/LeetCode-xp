
# Solved in: 34 m 3 sec
# 5/26/2025
# Runtime: 19 ms - beats 19.99%
# Memory: 17.60 mb - beats 96.45% 



class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        
        res = []

        cands = (i for i in range(left, right + 1) if "0" not in str(i)) # generator 

        for i in cands:

            if any([i % int(x) for x in str(i)]):
                continue
            res.append(i)

        return res



it = Solution()
result = it.selfDividingNumbers(47, 85)
print(result)
