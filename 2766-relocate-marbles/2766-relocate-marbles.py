class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        marbleMap = {i: 0 for i in nums}
        for i in nums:
            marbleMap[i] += 1
        
        for i in range(len(moveTo)):
            toShift = marbleMap[moveFrom[i]]
            marbleMap[moveFrom[i]] = 0
            if moveTo[i] not in marbleMap:
                marbleMap[moveTo[i]] = 0
            marbleMap[moveTo[i]] += toShift
            
            if marbleMap[moveFrom[i]] == 0:
                del marbleMap[moveFrom[i]]
        
        return sorted(marbleMap.keys())