class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        h = []
        for i in range(len(heights) - 1):
            if heights[i + 1] - heights[i] <= 0:
                continue
            heappush(h, heights[i + 1] - heights[i])
            if len(h) > ladders:
                smallestGap = heappop(h)
                if smallestGap > bricks:
                    return i
                bricks -= smallestGap
        return len(heights) - 1