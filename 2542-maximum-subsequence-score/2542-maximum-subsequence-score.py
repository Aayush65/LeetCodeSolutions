class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        nums = [[i, j] for i, j in zip(nums2, nums1)]
        nums.sort(reverse=True)
        
        h = []
        total = 0
        maxScore = 0
        for i, j in nums:
            total += j
            heappush(h, j)
            if len(h) == k:
                maxScore = max(maxScore, total * i)
                total -= heappop(h)
        return maxScore