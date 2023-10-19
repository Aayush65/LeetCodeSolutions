def backspacedString(s: str) -> str:
    final_s = ""
    i = 0
    while i < len(s):
        if s[i] == "#":
            final_s = final_s[:-1]
        else:
            final_s += s[i]
        i += 1
    return final_s

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = backspacedString(s)
        t = backspacedString(t)
        return True if s == t else False