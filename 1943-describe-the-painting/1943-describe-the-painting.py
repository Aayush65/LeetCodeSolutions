class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        segmentDict = defaultdict(int)
        for i, j, k in segments:
            segmentDict[i] += k
            segmentDict[j] -= k
        
        color = 0
        prev = 0
        res = []
        for i in sorted(segmentDict):
            if color:
                res.append([prev, i, color])
            prev = i
            color += segmentDict[i]
        return res