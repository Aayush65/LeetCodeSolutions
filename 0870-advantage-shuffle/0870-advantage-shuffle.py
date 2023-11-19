class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2 = [[x, i] for i, x in enumerate(nums2)]
        nums2.sort()
        nums1.sort()
        n = len(nums1)
        j = 0
        breaked = False
        for i in range(n):
            while j < n and nums1[j] <= nums2[i][0]:
                j += 1
            if j == n:
                breaked = True
                break
            nums2[i].append(nums1[j])
            nums1[j] = -1
        
        if breaked:
            j = 0
            for k in range(i, n):
                while j < n and nums1[j] == -1:
                    j += 1
                nums2[k].append(nums1[j])
                nums1[j] = -1
        
        res = [i[2] for i in sorted(nums2, key = lambda x: x[1])]
        return res