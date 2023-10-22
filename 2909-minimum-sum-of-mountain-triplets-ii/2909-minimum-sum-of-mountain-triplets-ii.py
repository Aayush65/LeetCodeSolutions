class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        minL = [float("inf")]
        mini = float("inf")
        for i in nums:
            mini = min(mini, i)
            minL.append(mini)
        minR = [float("inf")]
        mini = float("inf")
        for i in nums[::-1]:
            mini = min(mini, i)
            minR.append(mini)
        minR.reverse()
        
        res = float("inf")
        n = len(nums)
        for i in range(1, n - 1):
            if minL[i] >= nums[i] or minR[i + 1] >= nums[i]:
                continue
            res = min(res, nums[i] + minL[i] + minR[i + 1])
        return -1 if res == float("inf") else res