class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        curr = 0
        chance = colors[0]
        game = {'A': 0, 'B': 0}
        for i in colors:
            if chance != i:
                if curr > 2:
                    game[chance] += curr - 2
                chance = i
                curr = 0
            curr += 1
        if curr > 2:
            game[chance] += curr - 2

        return game['A'] > game['B']