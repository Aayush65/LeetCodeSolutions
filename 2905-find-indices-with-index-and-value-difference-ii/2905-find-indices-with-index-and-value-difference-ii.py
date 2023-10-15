class Solution:
    def findIndices(self, nums: List[int], d: int, v: int) -> List[int]:
        n = len(nums)
        from sortedcontainers import SortedList
        ordlist = SortedList(key=lambda x: x[0])
        for i in range(d, n):
            ordlist.add((nums[i], i))

        for i in range(n - d):
            smallIdx = ordlist.bisect_right((nums[i] - v, 0)) - 1
            if smallIdx > -1:
                return [i, ordlist[smallIdx][1]]
            bigIdx = ordlist.bisect_left((nums[i] + v, 0))
            if bigIdx < len(ordlist):
                return [ordlist[bigIdx][1], i]
            ordlist.remove((nums[i + d], i + d))
        
        return [-1, -1]