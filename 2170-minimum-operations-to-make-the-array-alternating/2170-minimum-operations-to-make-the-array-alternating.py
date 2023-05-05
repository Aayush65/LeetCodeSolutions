class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        even = {-1: 0}
        odd = {-1: 0}
        for i in range(len(nums)):
            if i % 2:
                if nums[i] not in even:
                    even[nums[i]] = 1
                else:
                    even[nums[i]] += 1
            else:
                if nums[i] not in odd:
                    odd[nums[i]] = 1
                else:
                    odd[nums[i]] += 1
            
        evenMax1 = evenMax2 = -1
        for i in even:
            if even[i] > even[evenMax1]:
                evenMax2 = evenMax1
                evenMax1 = i
            elif even[i] > even[evenMax2]:
                evenMax2 = i
                
        oddMax1 = oddMax2 = -1
        for i in odd:
            if odd[i] > odd[oddMax1]:
                oddMax2 = oddMax1
                oddMax1 = i
            elif odd[i] > odd[oddMax2]:
                oddMax2 = i
                
        if evenMax1 != oddMax1:
            return len(nums) - even[evenMax1] - odd[oddMax1]
        else:
            if evenMax2 == -1 and oddMax2 == -1:
                return len(nums) // 2
            if evenMax2 == -1:
                return len(nums) - even[evenMax1] - odd[oddMax2]
            if oddMax2 == -1:
                return len(nums) - even[evenMax2] - odd[oddMax1]
            return min(len(nums) - even[evenMax2] - odd[oddMax1], len(nums) - even[evenMax1] - odd[oddMax2])
        
