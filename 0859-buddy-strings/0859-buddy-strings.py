class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if sorted(s) != sorted(goal):
            return False
        first = -1
        for i in range(len(s)):
            if s[i] != goal[i]:
                if first != -1:
                    if s[first] != goal[i] or s[i] != goal[first]:
                        return False
                    first = -2
                elif first == -2:
                    return False
                else:
                    first = i
        return first == -2 or len(set(list(s))) != len(list(s))