class Solution:
    def canChange(self, start: str, target: str) -> bool:
        s1 = []
        s2 = []
        for i in range(len(start)):
            if start[i] != '_':
                s1.append([start[i], i])
            if target[i] != '_':
                s2.append([target[i], i])
        
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