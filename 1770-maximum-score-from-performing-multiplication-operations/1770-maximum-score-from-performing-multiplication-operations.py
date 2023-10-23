class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        nums = deque([(nums[i], i) for i in range(len(nums))])
        
        memo = {}
        def backtrack(index: int) -> int:
            if index == len(multipliers):
                return 0
            if (nums[0][1], nums[-1][1]) in memo:
                return memo[(nums[0][1], nums[-1][1])]
            
            left = nums.popleft()
            takeLeft = left[0] * multipliers[index] + backtrack(index + 1)
            nums.appendleft(left)
            
            right = nums.pop()
            takeRight = right[0] * multipliers[index] + backtrack(index + 1)
            nums.append(right)
            
            res = max(takeLeft, takeRight)
            
            memo[(nums[0][1], nums[-1][1])] = res
            return res
            
        return backtrack(0)