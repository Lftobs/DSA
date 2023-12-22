'''
Link: https://leetcode.com/problems/reverse-integer/
'''
class Solution:
    def reverse(self, x: int) -> int:
        sign = '-' if x < 0 else None
        if x > 2**31 -1 or x < -2**31:
            return 0
        if  int(str(abs(x))[::-1]) > 2**31 -1:
                return 0
        return int(str(abs(x))[::-1]) if sign == None  else -int(str(abs(x))[::-1])
