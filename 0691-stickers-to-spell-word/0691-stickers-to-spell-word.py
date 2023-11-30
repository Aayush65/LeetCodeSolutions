class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        indexOf = lambda x: ord(x) - ord('a')
        
        def wordToFreq(s: int) -> list[int]:
            freq = [0] * 26
            for i in s:
                freq[indexOf(i)] += 1
            return tuple(freq)
        
        stickers = [wordToFreq(i) for i in stickers]

        @cache
        def dp(target: list[int]) -> int:
            if sum(target) == 0:
                return 0
            res = float("inf")
            for word in stickers:
                newTarget = []
                isChanged = False
                for i in range(26):
                    newTarget.append(max(0, target[i] - word[i]))
                    if target[i] != newTarget[-1]:
                        isChanged = True
                if not isChanged:
                    continue
                newTarget = tuple(newTarget)
                res = min(res, 1 + dp(newTarget))
            return res
        
        res = dp(wordToFreq(target))
        return res if res != float("inf") else -1