class Solution:
    def bestClosingTime(self, customers: str) -> int:
        lastHour = 0
        for i in customers:
            lastHour += 1 if i == 'Y' else 0

        minPenalty = lastHour
        minPenIndex = 0
        for i in range(len(customers)):
            lastHour += -1 if customers[i] == 'Y' else 1
            if lastHour < minPenalty:
                minPenalty = lastHour
                minPenIndex = i + 1

        return minPenIndex