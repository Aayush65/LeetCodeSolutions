class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        nums = []
        hs = set()
        for i in range(len(grid)):
            num = 0
            bitIdx = 0
            for j in grid[i][::-1]:
                num += j * (2 ** bitIdx)
                bitIdx += 1
            if not num:
                return [i]
            if num in hs:
                continue
            hs.add(num)
            nums.append((num, i))

        res = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i][0] & nums[j][0] == 0:
                    return sorted([nums[i][1], nums[j][1]])
        return []