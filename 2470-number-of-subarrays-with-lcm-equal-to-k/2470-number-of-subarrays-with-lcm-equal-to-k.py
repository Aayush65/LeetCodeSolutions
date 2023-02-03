class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            if k % nums[i]:
                continue
            currLCM = nums[i]
            for j in range(i, len(nums)):
                currLCM = lcm(nums[j], currLCM)
                if currLCM > k:
                    break
                if currLCM == k:
                    count += 1
        return count