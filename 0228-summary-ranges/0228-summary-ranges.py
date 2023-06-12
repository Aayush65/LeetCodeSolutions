class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        start = end = float("inf")
        for i in range(len(nums)):
            if nums[i] != end + 1:
                if start != float("inf") and start == end:
                    ranges.append(str(start))
                elif start != end:
                    ranges.append(str(start) + "->" + str(end))
                start = nums[i]
            end = nums[i]
        if start != float("inf") and start == end:
            ranges.append(str(start))
        elif start != end:
            ranges.append(str(start) + "->" + str(end))
        return ranges