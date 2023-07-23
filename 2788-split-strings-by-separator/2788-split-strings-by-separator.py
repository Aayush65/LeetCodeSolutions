class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        newWords = []
        for i in words:
            word = i.split(separator)
            for j in word:
                if j:
                    newWords.append(j)
        return newWords