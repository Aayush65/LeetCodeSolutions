class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        nums = []
        for i in grid:
            num = 0
            bitIdx = 0
            for j in i[::-1]:
                num += j * (2 ** bitIdx)
                bitIdx += 1
            nums.append(num)
        
        res = []
        for i in range(len(nums)):
            if not nums[i]:
                return [i]
            for j in range(len(nums)):
                if nums[i] & nums[j] == 0:
                    return sorted([i, j])
        return []