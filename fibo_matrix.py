# coding: utf-8
# Your code here!
import numpy as np

def fibo(n):
    arr = np.matrix([[1, 1], [1, 0]])
    fibo_arr = arr**n
    print(fibo_arr[1, 0])
    
fibo(10)

# -> 55

import numpy as np

class Solution:
    def fib(self, N: int) -> int:
        arr = np.matrix([[1, 1], [1, 0]])
        fibo_arr = arr**N
        return fibo_arr[1, 0]