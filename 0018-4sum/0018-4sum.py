class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        nums.sort()
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                newTarget = target - nums[i] - nums[j]
                a, b = j + 1, len(nums) - 1
                while a < b:
                    if nums[a] + nums[b] < newTarget:
                        a += 1
                    elif nums[a] + nums[b] > newTarget:
                        b -= 1
                    else:
                        res.add((nums[i], nums[j], nums[a], nums[b]))
                        a += 1
                        b -= 1
        return res