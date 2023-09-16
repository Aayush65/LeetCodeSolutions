class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        even = [0]
        odd = [0]
        for i in range(len(nums)):
            if i % 2:
                odd.append(odd[-1] + nums[i])
            else:
                even.append(even[-1] + nums[i])
        
        count = 0
        for i in range(len(nums)):
            evenSide = even[(i + 1)// 2] + odd[-1] - odd[(i + 1)// 2] 
            oddSide = odd[i // 2] + even[-1] - even[i // 2 + 1]

            if evenSide == oddSide:
                count += 1
        return count