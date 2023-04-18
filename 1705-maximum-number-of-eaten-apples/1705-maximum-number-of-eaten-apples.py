class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        appleHeap = []
        countDays = 0
        day = 0
        for i in range(len(apples)):
            if apples[i]:
                heappush(appleHeap, [i + days[i], apples[i]])
            while appleHeap and appleHeap[0][0] <= i:
                heappop(appleHeap)
            if appleHeap:
                if appleHeap[0][1] == 1:
                    heappop(appleHeap)
                else:
                    appleHeap[0][1] -= 1
                countDays += 1
            day += 1
        
        while appleHeap:
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