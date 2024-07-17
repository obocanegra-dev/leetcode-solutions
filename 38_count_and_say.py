class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "1"
        
        current = "1"
        
        for _ in range(2, n + 1):
            next_seq = ""
            count = 1
            for j in range(1, len(current)):
                if current[j] == current[j - 1]:
                    count += 1
                else:
                    next_seq += str(count) + current[j - 1]
                    count = 1
            next_seq += str(count) + current[-1]
            current = next_seq
        
        return current
