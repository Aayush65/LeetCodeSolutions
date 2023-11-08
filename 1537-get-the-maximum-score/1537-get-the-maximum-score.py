class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        common = set(nums1).intersection(set(nums2))
        section1 = []
        curr = 0
        for i in nums1:
            if i in common:
                section1.append(curr)
                curr = 0
            else:
                curr += i
        section1.append(curr)
        
        section2 = []
        curr = 0
        for i in nums2:
            if i in common:
                section2.append(curr)
                curr = 0
            else:
                curr += i
        section2.append(curr)
        # print(section1)
        # print(section2)
        
        res = sum(max(section1[i], section2[i]) for i in range(len(section1))) + sum(common)
        return res % int(1e9 + 7)