class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjMap = defaultdict(list)
        for i, j in adjacentPairs:
            adjMap[i].append(j)
            adjMap[j].append(i)
            
        start = end = float("inf")
        for i in adjMap:
            if len(adjMap[i]) == 1:
                start = i
                break
        
        arr = [start, adjMap[start][0]]
        n = len(adjMap)
        while len(arr) < n:
            if adjMap[arr[-1]][0] == arr[-2]:
                arr.append(adjMap[arr[-1]][1])
            else:
                arr.append(adjMap[arr[-1]][0])
        return arr
                
        