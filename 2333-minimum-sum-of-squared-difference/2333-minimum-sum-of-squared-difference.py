class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        nums = sorted([-abs(i- j) for i, j in zip(nums1, nums2)])
        k = k1 + k2
        n = len(nums)
        if k > -sum(nums):
            return 0
        
        while k:
            diff = -heappop(nums)
            nextDiff = max(k // n, 1) if nums else k
            diff -= nextDiff
            k -= nextDiff
            heappush(nums, -diff)
        
        return sum(i ** 2 for i in nums)