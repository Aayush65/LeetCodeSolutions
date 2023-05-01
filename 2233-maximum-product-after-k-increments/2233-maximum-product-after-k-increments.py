class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapify(nums)
        while k:
            k -= 1
            smallest = heappop(nums)
            smallest += 1
            heappush(nums, smallest)
        mul = 1
        for i in nums:
            mul = (mul * i) % 1000000007
        return mul 
            