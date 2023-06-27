class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        preSum = []
        total = 0
        for i in nums:
            total += i
            preSum.append(total)

        mod = int(1e9 + 7)
        res = 0

        for i in range(len(nums)):
            if preSum[i] * 3 > total: break
            j = bisect_left(preSum, 2 * preSum[i], i + 1)
            k = bisect_right(preSum, (preSum[i] + total) // 2, j + 1)
            if k > len(nums) or preSum[k - 1] > (preSum[i] + total) // 2:
                continue
            k = min(k, len(nums) - 1)
            res = (res + k - j) % mod
        return res