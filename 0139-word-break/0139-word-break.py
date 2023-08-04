class Solution:
    def wordBreak(self, s: str, wordDict: List[str], i: int = 0) -> bool:
        indexMap = {len(s): True}
        def wordBreakDP(index: int) -> bool:
            if index in indexMap:
                return indexMap[index]
            i = 0
            res = False
            while i < len(wordDict):
                ifDictInS = False
                if len(s) - index >= len(wordDict[i]):
                    ifDictInS = True
                    for j in range(len(wordDict[i])):
                        if wordDict[i][j] != s[index+j]:
                            ifDictInS = False
                            break
                if ifDictInS:
                    res |= wordBreakDP(index+len(wordDict[i]))
                    if res:
                        break
                i += 1
            indexMap[index] = res
            return res
        return wordBreakDP(0)