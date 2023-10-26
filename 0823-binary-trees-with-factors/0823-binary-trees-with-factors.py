class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        mod = int(1e9 + 7)
        
        arrSet = set(arr)
        indexMap = {arr[i]: i for i in range(len(arr))}
        
        @cache
        def dp(n: int) -> int:
            index = indexMap[n]
            res = 1
            for i in range(index):
                if arr[index] % arr[i] or arr[index] // arr[i] not in arrSet:
                    continue
                res += dp(arr[i]) * dp(arr[index] // arr[i])
                res %= mod
            return res
            
            
        return sum(dp(i) for i in arr) % mod