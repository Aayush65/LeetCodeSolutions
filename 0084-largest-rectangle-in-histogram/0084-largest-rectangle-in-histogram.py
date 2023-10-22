class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        n = len(heights)
        maxArea = 0
        stack = []
        for i in range(n):
            index = i
            while stack and stack[-1][1] > heights[i]:
                currArea = stack[-1][1] * (i - stack[-1][0])
                maxArea = max(maxArea, currArea)
                index = stack[-1][0]
                stack.pop()
            stack.append((index, heights[i]))
            
        return maxArea  