class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        indexOf = lambda x: ord(x) - ord('A')
        freq = [0] * 26
        for i in tiles:
            freq[indexOf(i)] += 1
        
        def backtrack(index: int) -> int:
            res = 0
            for i in range(26):
                if freq[i]:
                    freq[i] -= 1
                    res += 1 + backtrack(index + 1)
                    freq[i] += 1
            return res
        
        return backtrack(0)