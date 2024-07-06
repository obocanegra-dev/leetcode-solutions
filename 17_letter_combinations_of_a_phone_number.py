class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtrack(combination, next_digits):
            if not next_digits:
                result.append(combination)
                return
            
            for letter in digit_map[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])
        
        result = []
        backtrack("", digits)
        return result
