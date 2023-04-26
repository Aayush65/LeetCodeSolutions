class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordLen = len(words[0])
        wordMap = {word: 0 for word in words}
        for word in words:
            wordMap[word] += 1

        res = []
        for i in range(len(s) - wordLen * len(words) + 1):
            currMap = defaultdict(int)
            for j in range(len(words)):
                currWord = []
                for k in range(wordLen):
                    currWord.append(s[i + j * wordLen + k])
                currWord = ''.join(currWord)
                if currWord in wordMap and currMap[currWord] < wordMap[currWord]:
                    currMap[currWord] += 1
                else:
                    j -= 1
                    break
            if j == len(words) - 1:
                res.append(i)

        return res