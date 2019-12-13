# coding: utf-8
# Your code here!
def reverseNumber(n):
    reversedNumber = 0
    while n > 0:
        remainNumber = n % 10
        reversedNumber = (reversedNumber * 10) + remainNumber
        n //= 10
    print(reversedNumber)

reverseNumber(123)

class Solution:
    def reverse(self, x: int) -> int:
        reversedNumber = 0
        x_saved = x
        if x < 0:
            x *= -1
        while x > 0:
            firstDigitNumber = x % 10
            reversedNumber = reversedNumber * 10 + firstDigitNumber
            x //= 10
        if (-2)**31 <= reversedNumber <= 2**31 - 1:
            if x_saved >= 0:
                return reversedNumber
            else:
                return -1*reversedNumber
        else:
            return 0
