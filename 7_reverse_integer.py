class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        negative = False
        if x < 0:
            negative = True
            x = -x
        
        reversed_x = 0
        while x > 0:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10
        
        if reversed_x > INT_MAX:
            return 0
        
        return -reversed_x if negative else reversed_x
