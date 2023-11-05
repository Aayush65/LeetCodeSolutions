class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        winMap = {i: [] for i in range(n)}
        for winner, loser in edges:
            winMap[loser].append(winner)
        
        winner = -1
        for i in winMap:
            if not winMap[i]:
                if winner != -1:
                    return -1
                winner = i
        return winner