class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        from sortedcontainers import SortedList
        
        n = len(nums1)
        
        # count1: the ends are original
        # count2: the ends are exchanged
        count1 = 0
        count2 = 1
        for k in range(n - 1):
            i, j = nums1[k], nums2[k]
            if max(i, j) <= min(nums1[-1], nums2[-1]):
                continue
            if min(i, j) > min(nums1[-1], nums2[-1]) or max(i, j) > max(nums1[-1], nums2[-1]):
                return -1
            if i > nums1[-1] or j > nums2[-1]:
                count1 += 1
            elif i > nums2[-1] or j > nums1[-1]:
                count2 += 1
        return min(count1, count2)