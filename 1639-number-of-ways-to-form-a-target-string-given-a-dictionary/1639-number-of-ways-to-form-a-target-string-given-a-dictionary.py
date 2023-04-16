class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        if len(target) > len(words[0]):
            return 0
        n = len(words)
        wordLen = len(words[0])
        freqMaps = [[0] * 26 for i in range(wordLen)]
        indexOf = lambda x: ord(x) - ord('a')

        for i in range(wordLen):
            for j in range(n):
                freqMaps[i][indexOf(words[j][i])] += 1
        mod = 1000000007

        @cache
        def dp(indexWord: int, indexTarget: int) -> int:
            if indexTarget == len(target):
                return 1
            if indexWord == wordLen:
                return 0
            res = dp(indexWord + 1, indexTarget) % mod
            currCharCount = freqMaps[indexWord][indexOf(target[indexTarget])]
            if currCharCount:
                res += currCharCount * dp(indexWord + 1, indexTarget + 1)
            return res % mod
        
        return dp(0, 0)
                