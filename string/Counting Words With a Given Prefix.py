


class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        
        # return len([i for i in words if i.startswith(pref)])

        count = 0

        for i in words:
            if i.startswith(pref):
                count += 1

        return count 




it = Solution()
result = it.prefixCount(["pay","attention","practice","attend"], "at")
print(result)
