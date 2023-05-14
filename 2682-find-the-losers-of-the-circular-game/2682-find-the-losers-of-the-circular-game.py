class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        losers = {i + 1 for i in range(n)}
        ballMap = defaultdict(int)
        
        i = 1
        player = 1
        ballMap[player] += 1
        losers.remove(1)
        while True:
            player = (player - 1 + k * i) % n + 1
            i += 1
            ballMap[player] += 1
            if player in losers:
                losers.remove(player)
            if ballMap[player] == 2:
                break
        return sorted(list(losers))