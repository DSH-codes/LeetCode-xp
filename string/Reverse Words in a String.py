
# Solved in 5 m 29 sec
# 5/9/2025 11:19 PM
# Runtime: 0ms - beats 100.00%


class Solution:
    def reverseWords(self, s: str) -> str:

        s = s.split()
        s = s[::-1]
        s = [i + ' ' for i in s]
        s = "".join(s)

        return s.strip()


it = Solution()

result = it.reverseWords("the sky is blue")

print(result)
