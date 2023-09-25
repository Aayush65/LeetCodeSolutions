class Solution:
    def countVowels(self, word: str) -> int:
        count = 0
        n = len(word)
        for i in range(n):
            if word[i] in {'a', 'e', 'i', 'o', 'u'}:
                count += (i + 1) * (n - i)
        return count
    
    
# n + (n - 1) + ... + 2 + 1
# 3 + 2 + 1
# n (n + 1) / 2