import bisect
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        lis = []
        for i, obstacle in enumerate(obstacles):
            if not lis or obstacle >= lis[-1]:
                idx = len(lis)
                lis.append(obstacle)
            else:
                idx = bisect.bisect(lis, obstacle)
                lis[idx] = obstacle
            obstacles[i] = idx + 1
        return obstacles