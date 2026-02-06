 

# solved in 6 minutes; Feb 2 2026 


class Solution:
    def convertDateToBinary(self, date: str) -> str:
        

        date = date.split("-")
        date = [bin(int(i)) for i in date]
        date = [i.removeprefix("0b") for i in date]

        return f"{date[0]}-{date[1]}-{date[2]}"

    


it = Solution()
result = it.convertDateToBinary("2080-02-29")
