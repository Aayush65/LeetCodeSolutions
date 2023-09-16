class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        h = []
        ch = nums[0]
        count = 0
        for i in nums:
            if ch == i:
                count += 1
            else:
                heappush(h, [-count, ch])
                count = 1
                ch = i
        heappush(h, [-count, ch])
        
        def countRemaining():
            count = 0
            for i, j in h:
                count -= i
            return count
        
        while h:
            count, x = heappop(h)
            count *= -1
            while count:
                if not h:
                    return count + countRemaining()
                nextCount, nextX = heappop(h)
                count -= 1
                nextCount += 1
                if nextCount:
                    heappush(h, [nextCount, nextX])
        return 0