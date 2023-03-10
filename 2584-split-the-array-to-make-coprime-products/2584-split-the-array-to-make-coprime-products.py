class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        def findPrimes(num: int) -> list[int]:
            primes = []
            if num % 2 == 0:
                primes.append(2)
            while num % 2 == 0:
                num //= 2
            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    primes.append(i)
                while num % i == 0:
                    num //= i
            if num > 1:
                primes.append(num)
            return primes

        # Calculating and storing prime factors
        primeFactors = []
        rightPrimes = defaultdict(int)
        for i in nums:
            pf = findPrimes(i)
            for j in pf:
                rightPrimes[j] += 1
            primeFactors.append(pf)
        # print(primeFactors)

        # Finding the leftmost element with no common primes
        overLap = set()
        for i in range(len(nums) - 1):
            for j in primeFactors[i]:
                rightPrimes[j] -= 1
                if j in rightPrimes and rightPrimes[j] > 0:
                    overLap.add(j)
                else:
                    if j in overLap:
                        overLap.remove(j)
            if not overLap:
                return i
        return -1