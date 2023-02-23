class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        business = [(capital[i], profits[i]) for i in range(len(profits))]
        business.sort(key = lambda x: (x[0], -x[1]))
        c, p = [], []
        for i in business:
            c.append(i[0])
            p.append(i[1])
        
        h = []
        capIndex = 0
        while k:
            while capIndex < len(c) and w >= c[capIndex]:
                heappush(h, -p[capIndex])
                capIndex += 1
            if h:
                w -= heappop(h)
            else:
                break
            k -= 1
        return w
            