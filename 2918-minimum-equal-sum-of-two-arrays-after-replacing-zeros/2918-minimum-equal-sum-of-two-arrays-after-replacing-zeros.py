class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:

        def calcVal(nums: list[int]) -> list[int]:
            total = zeroes = 0
            for i in nums:
                if i:
                    total += i
                else:
                    zeroes += 1
            total += zeroes
            if zeroes:
                zeroes = 1
            return [total, zeroes]
        
        t1, z1 = calcVal(nums1)
        t2, z2 = calcVal(nums2)
        
        if t1 > t2:
            if z2:
                return t1
        elif t2 > t1:
            if z1:
                return t2
        else:
            return t1
        return -1