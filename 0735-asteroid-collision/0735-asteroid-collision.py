class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            while i < 0 and stack and stack[-1] >= 0:
                poped = stack.pop()
                if abs(poped) == abs(i):
                    i = 0
                elif abs(poped) >= abs(i):
                    i = poped
            if not i:
                continue
            stack.append(i)
        return stack