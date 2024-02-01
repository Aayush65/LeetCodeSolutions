class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        hm = {}
        for i in nums2:
            while stack and stack[-1] < i:
                hm[stack.pop()] = i
            stack.append(i)
        
        res = []
        for i in nums1:
            if i in hm:
                res.append(hm[i])
            else:
                res.append(-1)
        return res