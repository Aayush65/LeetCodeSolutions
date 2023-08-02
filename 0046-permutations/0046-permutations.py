class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        included = set()

        def findPermutation(perm: list[int]) -> None:
            if len(perm) == len(nums):
                permutations.append(perm.copy())
            for i in range(len(nums)):    
                if i not in included:
                    included.add(i)
                    perm.append(nums[i])
                    findPermutation(perm)
                    perm.pop()
                    included.remove(i)

        findPermutation([])
        return permutations