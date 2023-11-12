# Trie Solution Not Working now (Only for python)

# class Trie:
#     def __init__(self, val: int):
#         self.val = val
#         self.children = [None, None]
        
#     def addNum(self, val: int, bitlen: int):
#         curr = self
#         for i in range(bitlen, -1, -1):
#             bit = (val >> i) & 1
#             if not curr.children[bit]:
#                 curr.children[bit] = Trie(bit)
#             curr = curr.children[bit]
            
#     def search(self, val: int, bitlen: int):
#         curr = self
#         maxNum = 0
#         for j in range(bitlen - 1, -1, -1):
#             bit = (i >> j) & 1
#             if curr.children[bit ^ 1]:
#                 bit ^= 1
#             maxNum |= bit << j
#             curr = curr.children[bit]
#         return val ^ maxNum
        
# class Solution:
#     def findMaximumXOR(self, nums: List[int]) -> int:
#         maxi = max(nums)
#         if not maxi:
#             return 0
#         bitlen = int(log2(maxi) + 1)
        
#         tr = Trie(0)
#         for i in nums:
#             tr.addNum(i, bitlen - 1)

#         res = 0
#         for i in nums:
#             res = max(res, tr.search(i, bitlen - 1))
#         return res

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        mask = res = 0
        for i in range(32, -1, -1):
            mask |= 1 << i
            valids = {i & mask for i in nums}
            
            temp = res | 1 << i
            for i in valids:
                if i ^ temp in valids:
                    res = temp
                    break
        return res