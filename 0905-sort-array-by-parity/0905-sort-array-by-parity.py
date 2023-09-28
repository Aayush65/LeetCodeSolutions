class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evens = []
        odds = []
        for i in nums:
            if i % 2:
                odds.append(i)
            else:
                evens.append(i)
        return evens + odds