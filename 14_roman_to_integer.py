class Solution(object):
    def romanToInt(self, s):
        roman_to_int_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }
        
        n = len(s)
        result = 0
        
        for i in range(n):
            if i < n - 1 and roman_to_int_map[s[i]] < roman_to_int_map[s[i+1]]:
                result -= roman_to_int_map[s[i]]
            else:
                result += roman_to_int_map[s[i]]
        
        return result
