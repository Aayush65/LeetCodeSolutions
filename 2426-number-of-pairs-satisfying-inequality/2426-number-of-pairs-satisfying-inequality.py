class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        differences = []
        for i, j in zip(nums1, nums2):
            differences.append(i - j)
        
        from sortedcontainers import SortedList
        sortedDiff = SortedList([])
        count = 0
        for i in differences:
            index = sortedDiff.bisect_right(i + diff)
            count += index
            sortedDiff.add(i)
        return count