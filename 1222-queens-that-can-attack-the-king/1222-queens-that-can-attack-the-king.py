class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        attackers = []
        queens = set(tuple(i) for i in queens)

        # going right
        for i in range(king[0] + 1, 8):
            if (i, king[1]) in queens:
                attackers.append([i, king[1]])
                break
        # going left
        for i in range(king[0] - 1, -1, -1):
            if (i, king[1]) in queens:
                attackers.append([i, king[1]])
                break
        # going down
        for j in range(king[1] + 1, 8):
            if (king[0], j) in queens:
                attackers.append([king[0], j])
                break
        # going up
        for j in range(king[1] - 1, -1, -1):
            if (king[0], j) in queens:
                attackers.append([king[0], j])
                break

        # going up-left
        for i in range(1, min(king) + 1):
            if (king[0] - i, king[1] - i) in queens:
                attackers.append([king[0] - i, king[1] - i])
                break
        # going up-right
        for i in range(1, min(king[0], 8 - king[1]) + 1):
            if (king[0] - i, king[1] + i) in queens:
                attackers.append([king[0] - i, king[1] + i])
                break
        # going down-left
        for i in range(1, min(8 - king[0], king[1]) + 1):
            if (king[0] + i, king[1] - i) in queens:
                attackers.append([king[0] + i, king[1] - i])
                break
        # going down-right
        for i in range(1, 8 - max(king)):
            if (king[0] + i, king[1] + i) in queens:
                attackers.append([king[0] + i, king[1] + i])
                break
        return attackers
