class Solution:
    def distMoney(self, money: int, children: int) -> int:
        dist = []
        for i in range(children):
            dist.append(1)
            money -= 1
        if money < 0:
            return -1
        count = 0
        for i in range(children):
            if money <= 0:
                break
            if money >= 7:
                money -= 7
                dist[i] += 7
                count += 1
            else:
                dist[-1] += money
                money = 0
        if dist[-1] == 4:
            if len(dist) == 1:
                return -1
            if dist[-2] == 8:
                count -= 1
        elif money:
            count -= 1
        return count