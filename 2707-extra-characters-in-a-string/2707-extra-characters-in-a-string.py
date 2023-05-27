class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        @cache
        def dp(index: int) -> int:
            if index == len(s):
                return 0
            res = 1 + dp(index + 1)
            for words in dictionary:
                if s[index: index + len(words)] == words:
                    res = min(res, dp(index + len(words)))
            return res
            
        return dp(0)