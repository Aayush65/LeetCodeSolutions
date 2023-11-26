class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        factor = k
        for i in range(int(k ** 0.5), k + 1):
            if k % i == 0 and i * i % k == 0:
                factor = i
                break
        
        vowels = {'a','e','i','o','u'}
        preSum = [(0, 0)]
        
        preSumMap = {(0, 0)}
        for i in s:
            curr = 0
            if i in vowels:
                curr = 1
            preSum.append((preSum[-1][0] + curr, preSum[-1][1] + 1 - curr))
            preSumMap.add(preSum[-1])
        maxV, maxC = preSum[-1]
        
        count = 0
        for v, c in preSum:
            if (v, c) not in preSumMap:
                continue
            curr = 0
            while v <= maxV and c <= maxC:
                if (v, c) in preSumMap:
                    preSumMap.remove((v, c))
                    curr += 1
                v += factor
                c += factor
            count += (curr * (curr - 1)) // 2
        return count