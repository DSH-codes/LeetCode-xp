
# Solved


def percentageLetter(s: str, letter: str) -> int:
        
        count = s.count(letter)

        return int(count / len(s) * 100)




result = percentageLetter("foobar", "x")

print(result)