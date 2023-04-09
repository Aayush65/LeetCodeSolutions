class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        diag = set()
        for i in range(len(nums)):
            diag.add(nums[i][i])
            diag.add(nums[i][len(nums) - i - 1])
        
        maxNum = max(diag) + 1
        primes = [True for i in range(maxNum)]
        primes[0] = primes[1] = False
        for i in range(2, maxNum):
            if not primes[i]:
                continue
            for j in range(i * i, maxNum, i):
                primes[j] = False
        
        maxPrime = 0
        for i in diag:
            if primes[i]:
                maxPrime = max(maxPrime, i)
        return maxPrime