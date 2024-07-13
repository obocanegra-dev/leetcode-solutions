class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words or len(s) < len(words) * len(words[0]):
            return []
        
        len_word = len(words[0])
        len_concatenated = len(words) * len_word
        word_count = len(words)
        
        target = {}
        for word in words:
            if word in target:
                target[word] += 1
            else:
                target[word] = 1
        
        result = []
        
        for i in range(len(s) - len_concatenated + 1):
            count = {}
            for j in range(word_count):
                word = s[i + j * len_word : i + (j + 1) * len_word]
                if word in target:
                    if word in count:
                        count[word] += 1
                    else:
                        count[word] = 1
                    if count[word] > target[word]:
                        break
                else:
                    break
            else:
                result.append(i)
        
        return result
