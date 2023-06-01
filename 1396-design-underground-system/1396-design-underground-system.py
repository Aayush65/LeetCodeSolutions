class UndergroundSystem:

    def __init__(self):
        self.checkinTime = {}
        self.avgMap = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkinTime[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, startTime = self.checkinTime[id]
        timeTaken = t - startTime
        if (start, stationName) in self.avgMap:
            self.avgMap[(start, stationName)] = (self.avgMap[(start, stationName)][0] + timeTaken, self.avgMap[(start, stationName)][1] + 1)
        else:
            self.avgMap[(start, stationName)] = (timeTaken, 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time, person = self.avgMap[(startStation, endStation)]
        return time / person


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)