class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) + len(nums2) != len(set(nums1 + nums2)):
            nums1 = set(nums1)
            repeats = 10
            for i in nums2:
                if i in nums1:
                    repeats = min(repeats, i)
            return repeats
        a = str(min(nums1))
        b = str(min(nums2))
        return min(int(a + b), int(b + a))