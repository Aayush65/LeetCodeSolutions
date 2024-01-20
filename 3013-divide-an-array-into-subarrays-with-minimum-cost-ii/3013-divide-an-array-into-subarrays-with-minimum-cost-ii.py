class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        from sortedcontainers import SortedList

        window = SortedList(nums[1: dist + 2])
        k, dist = k - 1, dist + 1
        currSum = sum(window[:k])
        res = currSum
        for i in range(1, len(nums) - dist):
            if k == dist:
                currSum += nums[i + dist] - nums[i]
                res = min(res, currSum)
                continue
            if nums[i] < window[k]:
                currSum += window[k] - nums[i]
            window.remove(nums[i])
            if nums[i + dist] < window[k - 1]:
                currSum += nums[i + dist] - window[k - 1]
            window.add(nums[i + dist])
            res = min(res, currSum)
        return res + nums[0]