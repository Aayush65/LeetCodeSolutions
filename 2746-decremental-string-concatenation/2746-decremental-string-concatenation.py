class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        
        @cache
        def dp(index: int, first: str, last: str) -> int:
            if index == len(words):
                return 0
            
            overlap = 0
            if last == words[index][0]:
                overlap = -1
            resStart = dp(index + 1, first, words[index][-1]) + overlap
            
            overlap = 0
            if first == words[index][-1]:
                overlap = -1
            resEnd = dp(index + 1, words[index][0], last) + overlap
            
            return min(resStart, resEnd) + len(words[index])
            
        return len(words[0]) + dp(1, words[0][0], words[0][-1])