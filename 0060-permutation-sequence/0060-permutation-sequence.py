class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        curr = [i + 1 for i in range(n)]
        for _ in range(k - 1):
            for i in range(n - 1, 0, -1):
                if curr[i - 1] < curr[i]:
                    break
            for j in range(n - 1, i - 1, -1):
                if curr[i - 1] < curr[j]:
                    curr[i - 1], curr[j] = curr[j], curr[i - 1]
                    break
            curr = curr[:i] + curr[i:][::-1]
            
        return "".join(str(i) for i in curr)