class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        indexMap = {i: [] for i in nums}
        dist = {i: 0 for i in nums}
        n = len(nums)
        
        calcDist = lambda i, j: (j - i) // 2
        for i in range(n):
            if indexMap[nums[i]]:
                currDist = calcDist(indexMap[nums[i]][-1], i)
                dist[nums[i]] = max(dist[nums[i]], currDist)
            indexMap[nums[i]].append(i)
        
        backDist = lambda i, j: (n - j + i) // 2 
        minDist = n
        for i in indexMap:
            s = indexMap[i][0]
            e = indexMap[i][-1]
            dist[i] = max(dist[i], backDist(s, e))
            minDist = min(minDist, dist[i])
        return minDist