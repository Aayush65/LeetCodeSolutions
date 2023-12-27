class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        back = 0
        for i in range(len(colors)-1):
            if colors[back] == colors[i+1]:
                if neededTime[back] >= neededTime[i+1]:
                    time += neededTime[i+1]
                else:
                    time += neededTime[back]
                    back = i+1
            else:
                back =  i + 1
        return time