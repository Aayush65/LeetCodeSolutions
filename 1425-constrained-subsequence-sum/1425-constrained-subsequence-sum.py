import heapq

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        h = [(-nums[0], 0)]
        res = nums[0]
        
        for i in range(1, len(nums)):
            while i - h[0][1] > k:
                heappop(h)

            curr = max(0, -h[0][0]) + nums[i]
            res = max(res, curr)
            heappush(h, (-curr, i))

        return res