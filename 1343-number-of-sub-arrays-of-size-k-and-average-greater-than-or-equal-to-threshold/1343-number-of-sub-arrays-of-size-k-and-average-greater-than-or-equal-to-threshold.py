class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        preSum = [0]
        for i in arr:
            preSum.append(preSum[-1] + i)
        
        subarrs = 0
        for i in range(len(preSum) - k):
            avg = (preSum[i + k] - preSum[i]) / k
            if avg >= threshold:
                subarrs += 1
        return subarrs
                