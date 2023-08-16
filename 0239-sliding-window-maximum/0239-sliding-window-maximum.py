class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        heapmap = defaultdict(int)
        for i in range(k):
            heapmap[-nums[i]] += 1
            heappush(heap, -nums[i])
        
        i, j = 0, k
        res = [-heap[0]]
        while j < len(nums):
            heappush(heap, -nums[j])
            heapmap[-nums[i]] -= 1
            heapmap[-nums[j]] += 1
            j += 1
            i += 1
            while not heapmap[heap[0]]:
                heappop(heap)
            res.append(-heap[0])
        return res