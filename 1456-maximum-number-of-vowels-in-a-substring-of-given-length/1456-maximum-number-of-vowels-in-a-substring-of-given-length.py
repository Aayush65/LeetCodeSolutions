class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowelMap = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        vowels = [0] * 5
        for i in range(k):
            if s[i] in vowelMap:
                vowels[vowelMap[s[i]]] += 1
        maxVowels = sum(vowels)

        for i in range(k, len(s)):
            if s[i] in vowelMap:
                vowels[vowelMap[s[i]]] += 1
            if s[i - k] in vowelMap:
                vowels[vowelMap[s[i - k]]] -= 1
            maxVowels = max(maxVowels, sum(vowels))
        return maxVowels