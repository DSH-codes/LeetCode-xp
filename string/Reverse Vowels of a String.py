
# Solved in: 9m 26 sec 
# 5/10/2025
# Runtime: 111ms - beats 5.02% 


class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = "aeiouAEIOU"

        vowels_from = [i for i in s if i in vowels][::-1]

        string_with_no_vowels = "".join([i if i not in vowels else "/" for i in s])

        for i in vowels_from:
            string_with_no_vowels = string_with_no_vowels.replace("/", i, 1)

        return string_with_no_vowels

it = Solution()

print(it.reverseVowels("IceCreAm"))


