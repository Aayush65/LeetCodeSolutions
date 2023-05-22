class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {i: 0 for i in nums}
        for i in nums:
            hashmap[i] += 1
        h = [(hashmap[i], i) for i in set(nums)]
        h.sort(reverse=True)
        return [h[i][1] for i in range(k)]
        