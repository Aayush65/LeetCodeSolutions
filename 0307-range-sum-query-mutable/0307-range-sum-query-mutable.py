class SegmentTree:
    def __init__(self, nums: list[int]):
        n = len(nums) + 1
        self.nums = [0] * (n - 1)
        self.rangeVals = [0] * n
        for i in range(n - 1):
            self.update(i, nums[i])
        
        
    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        index += 1
        while index < len(self.rangeVals):
            self.rangeVals[index] += diff
            index += index & -index
    
    def rangeQuery(self, left: int, right: int) -> int:
        total = 0
        right += 1
        while right > 0:
            total += self.rangeVals[right]
            right -= right & -right
        while left > 0:
            total -= self.rangeVals[left]
            left -= left & -left
        return total
        

class NumArray:

    def __init__(self, nums: list[int]):
        self.st = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.st.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.st.rangeQuery(left, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)