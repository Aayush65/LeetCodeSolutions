class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        numMap = [0] * 32
        indexOf = lambda x: int(log2(x))
        total = 0
        for i in nums:
            total += i
            numMap[indexOf(i)] += 1

        if total < target:
            return -1

        def isPossible(k):
            total = k
            for i in range(31, -1, -1):
                val = 2 ** i
                if val > total:
                    continue
                remainder = total % val
                total -= numMap[i] * val
                if total < 0:
                    total = remainder
            return total == 0

        req = [0] * int(log2(target) + 1)
        tempTar = target
        for i in range(len(req) - 1, -1, -1):
            val = 2 ** i
            if val <= target:
                target -= val
                req[i] += 1

        target = tempTar
        ops = 0
        for i in range(len(req)):
            if req[i] == 0:
                continue
            if numMap[i]:
                numMap[i] -= 1
                req[i] -= 1
                continue
            if isPossible(2 ** i):
                temp = 2 ** i
                for j in range(i - 1, -1, -1):
                    val = 2 ** j
                    if val <= temp:
                        toUse = min(numMap[j], temp // val)
                        numMap[j] -= toUse
                        temp -= val * toUse                            
                continue
            for j in range(i + 1, len(numMap)):
                if numMap[j]:
                    ops += j - i
                    numMap[j] -= 1
                    req[i] -= 1
                    for k in range(i, j):
                        numMap[k] += 1
                    break
        return ops