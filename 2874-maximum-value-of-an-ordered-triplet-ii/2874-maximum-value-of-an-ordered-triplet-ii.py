class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        leftMax = [0]
        for i in nums:
            leftMax.append(max(leftMax[-1], i))
            
        rightMax = [0]
        for i in nums[::-1]:
            rightMax.append(max(rightMax[-1], i))
        rightMax.reverse()
        
        maxVal = 0
        for i in range(1, len(nums) - 1):
            maxVal = max(maxVal, (leftMax[i] - nums[i]) * rightMax[i + 1])
        return maxVal