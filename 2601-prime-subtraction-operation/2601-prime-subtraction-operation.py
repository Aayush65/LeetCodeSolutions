class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        maxP = max(nums) + 1
        primes = [1 for i in range(maxP)]
        primes[0] = primes[1] = 0
        for i in range(2, maxP):
            if not primes[i]: 
                continue
            for j in range(i * i, maxP, i):
                primes[j] = 0
        primes = [i for i in range(maxP) if primes[i]]
        primes.append(1001)
        for i in range(len(nums) - 1):
            limit = nums[i] - 1
            if i > 0:
                limit -= nums[i - 1]
            if limit in {1, 0}:
                continue
            idx = bisect_left(primes, limit)
            if primes[idx] != limit:
                idx -= 1
            if idx < 0:
                return False
            nums[i] -= primes[idx]
        return nums[-1] > nums[-2] if len(nums) > 1 else True