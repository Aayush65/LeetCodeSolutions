class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        total = 0
        for i in range(1, n + 1):
            total ^= i
        
        for i in range(n - 2, -1, -2):
            total ^= encoded[i]

        original = [total]
        for i in encoded:
            original.append(original[-1] ^ i)
        return original