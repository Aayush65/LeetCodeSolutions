class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = []
        i = j = 0
        while len(word) < len(word1) + len(word2):
            if i < len(word1) and (len(word) % 2 == 0 or j == len(word2)):
                word.append(word1[i])
                i += 1
            else:
                word.append(word2[j])
                j += 1
        return ''.join(word)