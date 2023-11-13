class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse = True)
        tasks.sort()
        maxTime = 0
        while tasks:
            time = processorTime.pop()
            for i in range(4):
                maxTime = max(time + tasks.pop(), maxTime)
        return maxTime