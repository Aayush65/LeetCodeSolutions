class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        diag = set()
        for i in range(len(nums)):
            diag.add(nums[i][i])
            diag.add(nums[i][len(nums) - i - 1])
                
        def isPrime(n):
            if n == 2 or n == 3: return True
            if n < 2 or n%2 == 0: return False
            if n < 9: return True
            if n%3 == 0: return False
            r = int(n**0.5)
            f = 5
            while f <= r:
                if n % f == 0: return False
                if n % (f+2) == 0: return False
                f += 6
            return True   
        
        maxPrime = 0
        for i in diag:
            if isPrime(i):
                maxPrime = max(maxPrime, i)
        return maxPrime