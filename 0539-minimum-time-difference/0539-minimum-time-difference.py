class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for i in timePoints:
            time = int(i[:2]) * 60 + int(i[3:])
            times.append(time)
        times.sort()
        minDiff = 24 * 60 + times[0] - times[-1]
        for i in range(1, len(times)):
            diff = times[i] - times[i - 1]
            minDiff = min(diff, minDiff)
        return minDiff