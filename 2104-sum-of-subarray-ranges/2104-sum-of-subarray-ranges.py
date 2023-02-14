class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            minH = []
            maxH = []
            for j in range(i, len(nums)):
                heappush(minH, nums[j])
                heappush(maxH, -nums[j])
                res += -maxH[0] - minH[0]
        return res