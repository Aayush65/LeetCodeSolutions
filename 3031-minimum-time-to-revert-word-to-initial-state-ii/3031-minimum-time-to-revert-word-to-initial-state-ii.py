class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
#         p = int(26639628671867)
#         indexOf = lambda x: ord(x) - ord('a')
        
#         hash1 = hash2 = 0
#         arr = []
#         currPow = 1
        
#         for i in range(len(word)):
#             x, y = word[i], word[-i - 1]
#             hash1 = (hash1 * 26 + indexOf(x)) % p
#             hash2 = (indexOf(y) * currPow + hash2) % p
#             arr.append(hash1 == hash2)
#             currPow = (currPow * 26) % p
        
#         arr.reverse()
#         for i in range(k, len(word), k):
#             if arr[i]:  return i // k
            
#         return ceil(len(word) / k)
            
        for i in range(k, len(word), k):
            if word.startswith(word[i:]):
                return i // k
        return ceil(len(word) / k)