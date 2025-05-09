


class Solution:
    
    def checkRecord(self, s: str) -> bool:

        counter = 0
        
        if s.count("A") > 1:
            return False

        if "LLL" in s:
            return False

        return True

it = Solution()

result = it.checkRecord("LPPALL")

print(result)
