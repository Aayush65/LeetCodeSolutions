class Trie:
    def __init__(self, val: int):
        self.val = val
        self.children = [None, None]
        self.count = 0
        
    def update(self, val: int, bitlen: int):
        curr = self
        for i in range(bitlen, -1, -1):
            bit = (val >> i) & 1
            if not curr.children[bit]:
                curr.children[bit] = Trie(bit)
            curr = curr.children[bit]
            curr.count += 1
    
    def remove(self, val: int, bitlen: int):
        if bitlen < 0:
            return
        bit = (val >> bitlen) & 1
        self.children[bit].count -= 1
        self.children[bit].remove(val, bitlen - 1)
        if not self.children[bit].count:
            self.children[bit] = None
        
    def search(self, val: int, bitlen: int):
        curr = self
        res = 0
        for i in range(bitlen, -1, -1):
            bit = (val >> i) & 1
            if curr.children[bit ^ 1]:
                bit ^= 1
            res |= bit << i
            curr = curr.children[bit]
        return val ^ res

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        tr = Trie(0)
        bitlen = int(log2(max(nums)))
        
        nums.sort()
        n = len(nums)
        j = 0
        res = 0
        for i in range(n):
            while j < n and nums[j] <= 2 * nums[i]:
                tr.update(nums[j], bitlen)
                j += 1
            res = max(res, tr.search(nums[i], bitlen))
            tr.remove(nums[i], bitlen)
        return res