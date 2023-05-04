class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = deque(list(senate))
        rToBoot = 0
        dToBoot = 0
        while senate:
            if senate[0] == 'R':
                if rToBoot:
                    rToBoot -= 1
                    senate.popleft()
                    continue
                dToBoot += 1
            else:
                if dToBoot:
                    dToBoot -= 1
                    senate.popleft()
                    continue
                rToBoot += 1
            senate.append(senate.popleft())
            if rToBoot == len(senate) or dToBoot == len(senate):
                break
        
        return 'Radiant' if senate[0] == 'R' else 'Dire'