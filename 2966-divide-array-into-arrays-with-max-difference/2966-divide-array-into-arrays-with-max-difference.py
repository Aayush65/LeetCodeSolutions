class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        i = j = 0
        flag = True
        curr = []
        for j in range(len(nums)):
            if nums[j] - nums[i] > k or len(curr) == 3:
                if j - i + 1 < 3 or len(curr) < 3:
                    flag = False
                    break
                res.append(curr.copy())
                i = j
                curr.clear()
            curr.append(nums[j])
        if j - i + 1 < 3 or len(curr) < 3:
            flag = False
        res.append(curr.copy())
        return res if flag else []