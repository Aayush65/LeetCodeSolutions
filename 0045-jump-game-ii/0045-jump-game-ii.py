class Solution:
    # Backtracking
    # def jump(self, nums: List[int]) -> int:
    #     hashmap = {len(nums) - 1: 0}

    #     def jumping(index: int = 0) -> None:
    #         if index >= len(nums):
    #             return 0
    #         if index in hashmap:
    #             return hashmap[index]
    #         minJumps = float("inf")
    #         for i in range(1, nums[index] + 1):
    #             minJumps = min(1 + jumping(index + i), minJumps)
    #         hashmap[index] = minJumps
    #         return minJumps

    #     return jumping()
    
    #Greedy
    def jump(self, nums: list[int]) -> int:
        i = j = 0
        jumps = 0
        while j < len(nums) - 1:
            farthest = j
            for k in range(i, j + 1):
                farthest = max(farthest, k + nums[k])
            i = j + 1
            j = farthest
            jumps += 1
        return jumps