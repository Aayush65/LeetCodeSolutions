class SegmentTree:

    def __init__(self, nums: List[int], identity_val: Optional[int], cmp: Callable, key: Callable = lambda x: x):
        self.n = len(nums)
        self.identity_val = identity_val
        self.key = key
        self.cmp = cmp

        self.nums = nums
        self.__build_nums()
        self.tree = [identity_val] * self.n * 2
        self.__build_tree()

    # Prints the segment tree when the Object is printed
    def __str__(self) -> str:
        return self.tree.__str__()
    
    # This function builds the main array at initial initialisation using key function
    def __build_nums(self):
        self.nums = [self.key(x) for x in self.nums]

    # This function builds the segment tree at initial initialisation
    def __build_tree(self):
        for i in range(self.n):
            self.tree[i + self.n] = self.nums[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.cmp(self.tree[2 * i], self.tree[2 * i + 1])

    # This function updates the values at the index to the new value
    def update(self, index: int, val: int):
        index += self.n
        self.tree[index] = val
        while index > 1:
            new_val = self.cmp(self.tree[index], self.tree[index ^ 1])
            index //= 2
            if self.tree[index] == new_val:
                break
            self.tree[index] = new_val

    # This function removes all the instances of the val from the tree
    def remove(self, val: int) -> int:
        removed = 0
        for i in range(self.n):
            if self.tree[self.n + i] == val:
                self.update(i, self.identity_val)
                removed += 1
        return removed

    # This function returns the result between the left and right indices (not inclusive)
    def query(self, left: int, right: int) -> int:
        res = self.identity_val
        left += self.n
        right += self.n
        # Uncomment the below to change this function to inclusive left and right pointers
        right += 1 
        while left < right:
            if left & 1:
                res = self.cmp(res, self.tree[left])
                left += 1
            if right & 1:
                right -= 1
                res = self.cmp(res, self.tree[right])
            left //= 2
            right //= 2
        return res
        
        
class NumArray:

    def __init__(self, nums: list[int]):
        self.st = SegmentTree(nums, identity_val= 0, cmp = lambda x1, x2: x1 + x2)

    def update(self, index: int, val: int) -> None:
        self.st.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.st.query(left, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)