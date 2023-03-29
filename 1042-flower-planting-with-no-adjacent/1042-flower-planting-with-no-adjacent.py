class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        pathMap = {i: set() for i in range(n)}
        for i, j in paths:
            pathMap[i - 1].add(j - 1)
            pathMap[j - 1].add(i - 1)
        
        flowers = [0] * n
        q = {i for i in range(n)}
        while q:
            poped = q.pop()
            if not flowers[poped]:
                flowers[poped] = 1
            for i in pathMap[poped]:
                if not flowers[i] or flowers[i] == flowers[poped]:
                    flowers[i] = flowers[poped] + 1
                    if flowers[i] == 5:
                        flowers[i] = 1
                    q.add(i)
        return flowers
                        