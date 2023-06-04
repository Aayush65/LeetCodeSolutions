class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:        
        rowVal = [[0, i, -1] for i in range(n)]
        colVal = [[0, -1] for i in range(n)]
                
        for i in range(len(queries)):
            typ, idx, val = queries[i]
            if typ == 0:
                rowVal[idx] = [val, rowVal[idx][1], i]
            else:
                colVal[idx] = [val, i]
                
        rowVal.sort(key = lambda x: -x[2])
        rowPreSum = [0]
        for i in rowVal:
            rowPreSum.append(rowPreSum[-1] + i[0])
        rowVal.reverse()
        rowPreSum.reverse()
            
        matSum = 0
        for val, priority in colVal:
            idx = bisect_left(rowVal, priority, key = lambda x: x[2])
            matSum += idx * val + rowPreSum[idx]
        return matSum