class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        allPlayers = set()
        winLoseMap = {}
        for w, l in matches:
            if w not in winLoseMap:
                winLoseMap[w] = 0
            if l in winLoseMap:
                winLoseMap[l] += 1
            else:
                winLoseMap[l] = 1
            allPlayers.add(w)
            allPlayers.add(l)

        oneTimeLosers = []
        winners = []
        for i in allPlayers:
            if winLoseMap[i] == 1:
                oneTimeLosers.append(i)
            elif winLoseMap[i] == 0:
                winners.append(i)

        winners.sort()
        oneTimeLosers.sort()
        return [winners, oneTimeLosers]