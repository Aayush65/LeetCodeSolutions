class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def isAP(i: int, j: int):
            if j - i < 1:
                return False
            
            minEle = float("inf")
            maxEle = -float("inf")
            allEle = set()
            for ele in range(i, j + 1):
                minEle = min(minEle, nums[ele])
                maxEle = max(maxEle, nums[ele])
                allEle.add(nums[ele])
                
            n = j - i + 1
            if (maxEle - minEle) % (j - i):
                return False
            diff = (maxEle - minEle) // (j - i)
            if not diff:
                return len(allEle) == 1
            for i in range(minEle + diff, maxEle, diff):
                if i not in allEle:
                    return False
            return True
        
        res = []
        for i in range(len(l)):
            res.append(isAP(l[i], r[i]))
        return res