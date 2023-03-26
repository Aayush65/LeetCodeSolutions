class Solution:
    def numSplits(self, s: str) -> int:
        hsLeft = set()
        hsRight = set()
        left = []
        right = []
        for i in range(len(s)):
            hsLeft.add(s[i])
            hsRight.add(s[-i - 1])
            left.append(len(hsLeft))
            right.append(len(hsRight))            
        right.reverse()
        
        count = 0
        for i in range(len(s) - 1):
            if left[i] == right[i + 1]:
                count += 1
        return count