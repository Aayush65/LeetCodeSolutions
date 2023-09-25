class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        freq = [0, 0, 0]
        n = len(s)

        indexOf = lambda x: ord(x) - ord('a')
        mul = lambda arr: arr[0] * arr[1] * arr[2]
        
        i, j = 0, 0
        while j < n:
            while j < n and not mul(freq):
                freq[indexOf(s[j])] += 1
                j += 1
            while mul(freq):
                count += n - j + 1
                freq[indexOf(s[i])] -= 1
                i += 1
        return count