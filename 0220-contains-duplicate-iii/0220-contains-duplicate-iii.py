class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        from sortedcontainers import SortedList
        sList = SortedList()
        freqMap = defaultdict(int)
        
        for i in range(min(indexDiff + 1, len(nums))):
            if not freqMap[nums[i]]:
                sList.add(nums[i])
            freqMap[nums[i]] += 1
            if freqMap[nums[i]] > 1:
                return True
            index = sList.index(nums[i])
            if index > 0 and nums[i] - sList[index - 1] <= valueDiff:
                return True
            if index < len(sList) - 1 and sList[index + 1] - nums[i] <= valueDiff:
                return True
        
        for i in range(indexDiff + 1, len(nums)):
            if not freqMap[nums[i]]:
                sList.add(nums[i])
            freqMap[nums[i]] += 1
            freqMap[nums[i - indexDiff - 1]] -= 1
            if not freqMap[nums[i - indexDiff - 1]]:
                sList.remove(nums[i - indexDiff - 1])
            if freqMap[nums[i]] > 1:
                return True
            index = sList.index(nums[i])
            if index > 0 and nums[i] - sList[index - 1] <= valueDiff:
                return True
            if index < len(sList) - 1 and sList[index + 1] - nums[i] <= valueDiff:
                return True
        
        return False