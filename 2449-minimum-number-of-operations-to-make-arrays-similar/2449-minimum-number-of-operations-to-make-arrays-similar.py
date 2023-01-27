class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums.sort()
        target.sort()
        evenNums = [i for i in nums if i % 2 == 0]
        oddNums = [i for i in nums if i % 2]
        evenTarget = [i for i in target if i % 2 == 0]
        oddTarget = [i for i in target if i % 2]
        
        inc = 0
        for i in range(len(evenNums) - 1, -1, -1):
            diff = evenTarget[i] - evenNums[i]
            if diff > 0:
                inc += diff // 2

        for i in range(len(oddNums) - 1, -1, -1):
            diff = oddTarget[i] - oddNums[i]
            if diff > 0:
                inc += diff // 2
        return inc


