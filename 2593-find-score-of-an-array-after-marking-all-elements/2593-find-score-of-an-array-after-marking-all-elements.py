class Solution:
    def findScore(self, nums: List[int]) -> int:
        minH = []
        for i in range(len(nums)):
            heappush(minH, (nums[i], i))
        marked = [0] * len(nums)
        score = 0
        while minH:
            val, idx = heappop(minH)
            if marked[idx]:
                continue
            marked[idx] = 1
            if idx > 0:
                marked[idx - 1] = 1
            if idx < len(nums) - 1:
                marked[idx + 1] = 1
            score += val
        return score