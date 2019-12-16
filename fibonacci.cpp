#include <iostream>
using namespace std;

class Solution {
public:
    int fib(int N) {
        if (N == 0) return 0;
        int a, b, c, a1, b1, c1, x, y, x1, y1;
        a = 1, b = 1, c = 0, x = 1, y = 0;
        N -= 1;
        while (N > 0) {
            if (N & 1) {
                x1 = x, y1 = y;
                x = a * x1 + b * y1;
                y = b * x1 + c * y1;
            }
            N /= 2;
            a1 = a, b1 = b, c1 = c;
            a = a1 * a1 + b1 * b1;
            b = b1 * (a1 + c1);
            c = b1 * b1 + c1 * c1;
        }
        return x;      
    }
};