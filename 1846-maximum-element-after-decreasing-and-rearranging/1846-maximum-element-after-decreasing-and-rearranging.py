class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        curr = 0
        for i in arr:
            if curr < i:
                curr += 1           
        return curr