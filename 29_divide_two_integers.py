class Solution:
    def divide(self, dividend, divisor):
        negative = (dividend < 0) != (divisor < 0)
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        temp = 0
        
        for i in range(31, -1, -1):
            if temp + (divisor << i) <= dividend:
                temp += divisor << i
                quotient |= 1 << i
        
        if negative:
            quotient = -quotient
        
        if quotient < -(2**31):
            return -(2**31)
        elif quotient > 2**31 - 1:
            return 2**31 - 1
        else:
            return quotient
