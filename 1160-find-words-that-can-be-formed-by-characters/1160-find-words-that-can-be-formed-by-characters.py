class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charFreq = Counter(chars)
        count = 0
        for word in words:
            freq = Counter(word)
            isGood = True
            for i in freq:
                if i not in charFreq or charFreq[i] < freq[i]:
                    isGood = False
                    break
            if isGood:
                count += len(word)
        return count