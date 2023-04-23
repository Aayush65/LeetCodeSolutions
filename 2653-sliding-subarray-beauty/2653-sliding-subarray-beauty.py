class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        count = [0] * 50
        for i in range(k):
            if nums[i] < 0:
                count[-nums[i] - 1] += 1
        tempx = x
        res = []
        for i in range(49, -1, -1):
            if count[i]:
                tempx -= count[i]
            if tempx <= 0:
                res.append(-i - 1)
                break
        if tempx > 0:
            res.append(0)
            
        for i in range(k, len(nums)):
            tempx = x
            if nums[i - k] < 0:
                count[-nums[i - k] - 1] -= 1
            if nums[i] < 0:
                count[-nums[i] - 1] += 1
            for j in range(49, -1, -1):
                if count[j]:
                    tempx -= count[j]
                if tempx <= 0:
                    res.append(-j - 1)
                    break
            if tempx > 0:
                res.append(0)
        return res