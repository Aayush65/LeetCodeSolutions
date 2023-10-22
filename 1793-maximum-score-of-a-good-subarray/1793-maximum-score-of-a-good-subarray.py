class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        maxScore = nums[k]
        i = j = k
        n = len(nums)
        currMin = nums[k]
        while i > 0 or j < n - 1:
            if i == 0 or (j < n - 1 and nums[j + 1] >= nums[i - 1]):
                j += 1
                currMin = min(currMin, nums[j])
            else:
                i -= 1
                currMin = min(currMin, nums[i])
            
            score = currMin * (j - i + 1)
            maxScore = max(maxScore, score)
        return maxScore