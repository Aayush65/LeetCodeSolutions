class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = [int(i) for i in version1.split('.')]
        version2 = [int(i) for i in version2.split('.')]
        while version1 and version1[-1] == 0:
            version1.pop()
        while version2 and version2[-1] == 0:
            version2.pop()
        # print(version1, version2)
        
        for v in range(max(len(version1), len(version2))):
            if v == len(version1):
                return -1
            if v == len(version2):
                return 1
            if version1[v] > version2[v]:
                return 1
            elif version1[v] < version2[v]:
                return -1
        return 0