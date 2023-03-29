class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = [i + 1 for i in range(len(pattern) + 1)]
        i = 0
        while i < len(pattern):
            j = i
            while j < len(pattern) and pattern[j] == 'D' and res[j + 1] > res[j]:
                j += 1
            if j != i:
                res = res[:i] + res[i: j + 1][::-1] + res[j + 1:]
                i = j
            else:
                i += 1
        return ''.join([str(i) for i in res])