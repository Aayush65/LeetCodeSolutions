class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        remaining = [(0, 0, 0)]
        for i in garbage[::-1]:
            last = remaining[-1]
            remaining.append((last[0] + i.count('M'), last[1] + i.count('P'), last[2] + i.count('G')))
        
        time = sum(remaining.pop())
        remaining.reverse()
        for i, t in enumerate(travel):
            trucks = 0
            if remaining[i][0]: trucks += 1
            if remaining[i][1]: trucks += 1
            if remaining[i][2]: trucks += 1
            time += trucks * t
        return time