class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: [x[0], x[1]])
        peopleMap = {i[0]: [] for i in people}
        for i, j in people:
            peopleMap[i].append(j)
        n = len(people)
        
        from sortedcontainers import SortedList
        freeIndices = SortedList([i for i in range(n)])
        res = [None] * n
        
        for i, _ in people:
            indices = []
            for k in peopleMap[i]:
                res[freeIndices[k]] = [i, k]
                indices.append(freeIndices[k])
            for k in indices:
                freeIndices.remove(k)
            peopleMap[i] = []
        return res