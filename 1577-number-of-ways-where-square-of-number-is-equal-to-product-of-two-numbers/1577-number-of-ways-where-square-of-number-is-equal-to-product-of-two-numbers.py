class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        count = 0
        map1 = {i: 0 for i in nums1}
        for i in nums1:
            map1[i] += 1
        map2 = {i: 0 for i in nums2}
        for i in nums2:
            map2[i] += 1
        
        count = 0
        for i in nums1:
            hm = map2.copy()
            for j in nums2:
                hm[j] -= 1
                if not hm[j]:
                    del hm[j]
                if (i * i) / j in hm:
                    count += hm[(i * i) / j]
        for i in nums2:
            hm = map1.copy()
            for j in nums1:
                hm[j] -= 1
                if not hm[j]:
                    del hm[j]
                if (i * i) / j in hm:
                    count += hm[(i * i) / j]
        return count