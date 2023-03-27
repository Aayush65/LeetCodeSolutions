class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
#         k = len(nums) - k
        
#         def quickSelect(l: int, r: int) -> int:
#             p = l
#             for i in range(l, r):
#                 if int(nums[i]) <= int(nums[r]):
#                     nums[p], nums[i] = nums[i], nums[p]
#                     p += 1
#             nums[p], nums[r] = nums[r], nums[p]
#             if p > k:
#                 return quickSelect(l, p - 1)
#             elif p < k:
#                 return quickSelect(p + 1, r)
#             else:
#                 return nums[p]
            
#         return quickSelect(0, len(nums) - 1)
        nums.sort(key = lambda x: int(x))
        return nums[-k]