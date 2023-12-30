class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq = defaultdict(int)
        for word in words:
            for i in word:
                freq[i] += 1
        
        for i in freq:
            if freq[i] % len(words):
                return False
        return True