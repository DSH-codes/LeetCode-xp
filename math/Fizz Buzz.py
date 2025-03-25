



class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result = [("FizzBuzz" if i%3 == 0 and i%5 == 0 else ("Fizz" if i%3 == 0 else ("Buzz" if i%5 == 0 else str(i)))) for i in range(1,n+1)]
        return result

it = Solution()
result = it.fizzBuzz(15)
print(result)
