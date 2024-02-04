class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        p = int(1e9 + 7)
        indexOf = lambda x: ord(x) - ord('a')
        
        def check(idx):
            j = len(word) - 1
            for i in range(idx, -1, -1):
                if word[i] != word[j]:
                    return False
                j -= 1
            return True
        
        
        hash1 = hash2 = 0
        arr = []
        currPow = 1
        
        for i in range(len(word)):
            x, y = word[i], word[-i - 1]
            hash1 = (hash1 * 26 + indexOf(x)) % p
            hash2 = (indexOf(y) * currPow + hash2) % p
            arr.append(hash1 == hash2)
            currPow = (currPow * 26) % p
        
        arr.reverse()
        for i in range(k, len(word), k):
            if arr[i]:  return i // k
            
        return ceil(len(word) / k)
            