class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        preSum = [0]
        for i in nums:
            preSum.append(preSum[-1] + i)

        res = [-1] * n
        for i in range(k, n - k):
            avg = (preSum[i + k + 1] - preSum[i - k]) // (2 * k + 1)
            res[i] = avg
        return res