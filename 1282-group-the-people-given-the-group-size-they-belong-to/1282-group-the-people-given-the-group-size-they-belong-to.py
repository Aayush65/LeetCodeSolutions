class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hm = defaultdict(list)
        res = []
        for i in range(len(groupSizes)):
            hm[groupSizes[i]].append(i)
            if len(hm[groupSizes[i]]) == groupSizes[i]:
                res.append(hm[groupSizes[i]])
                hm[groupSizes[i]] = []
        res.sort(key=lambda x: len(x))
        return res