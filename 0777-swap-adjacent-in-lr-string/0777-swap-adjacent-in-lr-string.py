class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        s1 = []
        s2 = []
        for i in range(len(start)):
            if start[i] != 'X':
                s1.append([start[i], i])
            if end[i] != 'X':
                s2.append([end[i], i])
        
        if len(s1) != len(s2):
            return False
        
        for i in range(len(s1)):
            if s1[i][0] != s2[i][0]:
                return False
            if s1[i][0] == 'L' and s1[i][1] < s2[i][1]:
                return False
            if s1[i][0] == 'R' and s1[i][1] > s2[i][1]:
                return False
        return True