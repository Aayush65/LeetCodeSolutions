class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        hm = defaultdict(int)
        haveAllVowels = lambda: hm['a'] and hm['e'] and hm['i'] and hm['o'] and hm['u']

        maxLen = 0
        i = j = 0
        prev = -1
        while j < len(word):
            if ord(word[j]) >= prev:
                prev = ord(word[j])
                hm[word[j]] += 1
                j += 1
            else:
                i = j
                prev = -1
                hm.clear()
            if haveAllVowels():
                maxLen = max(maxLen, j - i)
        return maxLen
            