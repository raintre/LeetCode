import math

class Solution:
    def fib(self, N: int) -> int:
        return (round((pow((1 + math.sqrt(5)) / 2, N) - pow((1 - math.sqrt(5)) / 2, N)) / math.sqrt(5)))
