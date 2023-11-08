class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        freq = {i: 0 for i in arr}
        for i in arr:
            freq[i] += 1
        arr.sort()
        mod = int(1e9 + 7)
        res = 0
        for i in range(len(arr)):
            count = 0
            freq[arr[i]] -= 1
            if freq[arr[i]] == 0:
                del freq[arr[i]]
            for j in range(i + 1, len(arr)):
                k = target - arr[i] - arr[j]  
                if k in freq:
                    count += freq[k]
                    if k == arr[j]:
                        count -= 1
            res += count // 2
            res %= mod
        return res