# (m - 1)本の→と(n - 1)本の↓の順列
import math

class Solution(object):
    def uniquePaths(self, m, n):
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))