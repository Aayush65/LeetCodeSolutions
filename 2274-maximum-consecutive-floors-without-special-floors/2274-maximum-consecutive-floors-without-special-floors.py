class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        special = deque(special)
        while special and top == special[-1]:
            special.pop()
            top -= 1
        while special and bottom == special[0]:
            special.popleft()
            bottom += 1
        if not special:
            return top - bottom + 1
        maxLen = max(special[0] - bottom, top - special[-1])
        for i in range(1, len(special)):
            maxLen = max(maxLen, special[i] - special[i - 1] - 1)
        return maxLen