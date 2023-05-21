class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        preSum = [0]
        for i in arr:
            preSum.append(preSum[-1] + i)
            
        minDiff = float("inf")
        minVal = float("inf")
        for i in range(max(arr) + 1):
            idx = bisect_left(arr, i)
            left = preSum[idx]
            right = (len(arr) - idx) * i
            diff = abs(target - left - right)
            if diff >= minDiff:
                break
            minDiff = diff
            minVal = i
        return minVal