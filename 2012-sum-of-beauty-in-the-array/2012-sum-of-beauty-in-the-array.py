class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        minMax = []
        mx = nums[0]
        for i in range(1, len(nums) - 1):
            minMax.append([mx])
            mx = max(mx, nums[i])
        mn = nums[-1]
        for i in range(len(nums) - 2, 0, -1):
            minMax[i - 1].append(mn)
            mn = min(mn, nums[i])

        res = 0
        for i in range(1, len(nums) - 1):
            prevMax, nextMin = minMax[i - 1]
            if prevMax < nums[i] < nextMin:
                res += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                res += 1
        return res