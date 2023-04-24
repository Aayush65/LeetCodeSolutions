class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapify(stones)
        while len(stones) > 1:
            a = -heappop(stones)
            b = -heappop(stones)
            a -= b
            if a:
                heappush(stones, -a)
        if not stones:
            return 0
        return -stones.pop()