class Solution(object):
    def intToRoman(self, num):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        roman_numeral = []
        
        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                roman_numeral.append(symbols[i])
        
        return ''.join(roman_numeral)
