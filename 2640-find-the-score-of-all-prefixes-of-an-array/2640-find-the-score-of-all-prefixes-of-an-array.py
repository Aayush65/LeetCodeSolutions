class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        maxList = []
        for i in nums:
            if not maxList or maxList[-1] <= i:
                maxList.append(i)
            else:
                maxList.append(maxList[-1])
        
        conver = nums.copy()
        for i in range(len(nums)):
            conver[i] += maxList[i]
            
        preSum = []
        for i in conver:
            if not preSum:
                preSum.append(i)
            else:
                preSum.append(preSum[-1] + i)
        return preSum