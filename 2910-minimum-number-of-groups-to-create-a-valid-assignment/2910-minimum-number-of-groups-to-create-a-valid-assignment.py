class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        numsMap = {i: 0 for i in nums}
        for i in nums:
            numsMap[i] += 1

        minLength = len(nums)
        for i in numsMap:
            minLength = min(minLength, numsMap[i])

        def minGroups(target: int, mini: int) -> int:
            count = 0
            while target % mini and target > mini - 2:
                count += 1
                target -= mini - 1
            if target and target < mini - 1:
                return 0
            count += target // mini
            return count

        def check(mini: int):
            groups = 0
            for i in numsMap:
                res = minGroups(numsMap[i], mini)
                if res:
                    groups += res
                else:
                    return 0
            return groups

        for i in range(minLength + 1, 0, -1):
            groups = check(i)
            if groups > 0:
                return groups