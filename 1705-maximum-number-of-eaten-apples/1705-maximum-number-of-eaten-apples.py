class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        appleHeap = []
        countDays = 0
        day = 0
        while appleHeap or day < len(apples):
            if day < len(apples) and apples[day]:
                heappush(appleHeap, [day + days[day], apples[day]])
            while appleHeap and appleHeap[0][0] <= day:
                heappop(appleHeap)
            if appleHeap:
                if appleHeap[0][1] == 1:
                    heappop(appleHeap)
                else:
                    appleHeap[0][1] -= 1
                countDays += 1
            day += 1
            
        return countDays