class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if len(h) < k:
                    heappush(h, [-nums1[i] - nums2[j], i, j])
                elif -h[0][0] > nums1[i] + nums2[j]:
                    heapreplace(h, [-nums1[i] - nums2[j], i, j])
                else:
                    break
        pairs = []
        for s, n1, n2 in h:
            pairs.append([nums1[n1], nums2[n2]])
        pairs.sort(key = lambda x: sum(x))
        return pairs