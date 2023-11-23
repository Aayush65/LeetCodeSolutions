class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        from sortedcontainers import SortedList
        eles = SortedList([nums[i] for i in range(k)])
        
        res = []
        for i in range(k, len(nums)):
            if k % 2:
                res.append(eles[k // 2])
            else:
                res.append((eles[k // 2] + eles[k // 2 - 1]) / 2)
            eles.remove(nums[i - k])
            eles.add(nums[i])
        if k % 2:
            res.append(eles[k // 2])
        else:
            res.append((eles[k // 2] + eles[k // 2 - 1]) / 2)
        return res