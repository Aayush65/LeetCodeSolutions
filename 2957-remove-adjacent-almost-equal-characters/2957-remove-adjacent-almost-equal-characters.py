class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        val = lambda x: ord(x) - ord('a')
        word = [val(i) for i in word]
        
        @cache
        def dp(index: int) -> int:
            if index >= len(word) - 1:
                return 0
            if abs(word[index] - word[index + 1]) < 2:
                return 1 + min(dp(index + 1), dp(index + 2))
            return dp(index + 1)
            
        return dp(0)