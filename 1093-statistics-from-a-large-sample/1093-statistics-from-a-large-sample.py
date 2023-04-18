class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        minEle = 255
        maxEle = 0
        n = 0
        total = 0
        
        mode = -1
        modeCount = 0
        for i in range(256):
            if count[i]:
                maxEle = i
            if count[-i - 1]:
                minEle = 256 - i - 1
            if count[i] > modeCount:
                modeCount = count[i]
                mode = i
            n += count[i]
            total += i * count[i]
        
        mean = total / n
        median = 0
        if n % 2:
            n //= 2
            for i in range(minEle, maxEle + 1):
                if n < count[i]:
                    median = i
                    break
                n -= count[i]
        else:
            n //= 2
            firstFound = False
            for i in range(minEle, maxEle + 1):
                if not firstFound and n <= count[i]:
                    median = i
                    firstFound = True
                if firstFound and n < count[i]:
                    median += i
                    median /= 2
                    break
                n -= count[i]
                
        return [minEle, maxEle, mean, median, mode]