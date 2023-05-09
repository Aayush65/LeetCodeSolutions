class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        preSum = [0]
        hm = {0: -1}
        maxArrLen = -1
        target = sum(nums) - x
        for i in range(len(nums)):
            preSum.append(preSum[-1] + nums[i])
            hm[preSum[-1]] = i
            if preSum[-1] - target in hm:
                maxArrLen = max(maxArrLen, i - hm[preSum[-1] - target])
            
        return len(nums) - maxArrLen if maxArrLen != -1 else -1