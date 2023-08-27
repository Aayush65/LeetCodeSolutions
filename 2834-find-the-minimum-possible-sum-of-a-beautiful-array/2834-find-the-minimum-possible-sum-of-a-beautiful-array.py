class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        total = 0
        notInc = set()
        i = 1
        while n:
            if i not in notInc:
                total += i
                notInc.add(target - i)
                n -= 1
            i += 1
        return total