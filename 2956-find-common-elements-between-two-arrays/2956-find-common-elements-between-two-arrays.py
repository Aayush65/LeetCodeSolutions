class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1, s2 = set(nums1), set(nums2)
        r1, r2 = 0, 0
        for i in nums1:
            if i in s2:
                r1 += 1
        for i in nums2:
            if i in s1:
                r2 += 1
        return [r1, r2]