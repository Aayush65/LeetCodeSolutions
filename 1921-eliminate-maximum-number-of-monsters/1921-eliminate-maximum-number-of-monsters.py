class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = [dist[i] / speed[i] for i in range(len(dist))]
        time.sort()
        
        monsters = 0
        for i in time:
            if monsters >= i:
                break
            monsters += 1
        return monsters