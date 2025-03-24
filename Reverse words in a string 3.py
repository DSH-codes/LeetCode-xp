
# Solved: 3/14/2025 3:06 AM

class Solution:
    def reverseWords(self, s: str) -> str:
        self.words = [i[::-1] + " " for i in s.split()]
        return "".join(self.words).rstrip()




it = Solution()
result = it.reverseWords("Mr Ding")
print(result)
