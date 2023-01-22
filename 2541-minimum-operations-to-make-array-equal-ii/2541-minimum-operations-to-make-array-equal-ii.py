class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        inc = 0
        dec = 0
        if k == 0:
            if nums1 == nums2:
                return 0
            else:
                return -1
        for i in range(n):
            diff = nums1[i] - nums2[i]
            if diff % k:
                return -1
            if diff < 0:
                dec -= diff // k
            else:
                inc += diff // k
        if inc != dec:
            return -1
        return inc
                
        