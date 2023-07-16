class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        freqMap = {i: 0 for i in nums}
        x = -1
        maxFreq = 0
        for i in nums:
            freqMap[i] += 1
            if freqMap[i] > maxFreq:
                maxFreq = freqMap[i]
                x = i
        
        if maxFreq * 2 <= n:
            return -1
        
        occurance = 0
        for i in range(len(nums)):
            if nums[i] == x:
                occurance += 1
            if occurance * 2 > i + 1 and (maxFreq - occurance) * 2 > n - i - 1:
                return i       
        return -1        