class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        zeroes = 0
        for i in nums:
            if i:
                zeroes = 0
                continue
            zeroes += 1
            count += zeroes
        return count