class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        preSum = [0]
        for i in nums:
            preSum.append(preSum[-1] + i)
        
        minLimit = 1
        for i in range(len(nums)):
            for j in range(i + minLimit, len(nums)):
                pre, post = 0, 0
                midIdx = (i + j) // 2
                if (j - i) % 2:
                    mid = ((nums[midIdx] + nums[midIdx + 1])) // 2
                else:
                    mid = nums[midIdx]
                pre = (midIdx - i + 1) * mid - preSum[midIdx + 1] + preSum[i]
                post = preSum[j + 1] - preSum[midIdx + 1] - (j - midIdx) * mid
                if pre + post <= k:
                    minLimit = max(minLimit, j - i + 1)
                else:
                    break
                
        return minLimit