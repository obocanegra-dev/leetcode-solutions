class Solution(object):
    def generateParenthesis(self, n):
        def backtrack(combination, left, right):
            if len(combination) == 2 * n:
                result.append("".join(combination))
                return
            if left < n:
                combination.append('(')
                backtrack(combination, left + 1, right)
                combination.pop()
            if right < left:
                combination.append(')')
                backtrack(combination, left, right + 1)
                combination.pop()
        
        result = []
        backtrack([], 0, 0)
        return result
