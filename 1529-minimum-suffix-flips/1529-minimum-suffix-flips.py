class Solution:
    def minFlips(self, target: str) -> int:
        target = str(int(target))
        if not int(target):
            return 0
        count = 0
        i = 0
        while i < len(target):
            if target[i] == '1':
                count += 1
                while i < len(target) and target[i] == '1':
                    i += 1
            else:
                count += 1
                while i < len(target) and target[i] == '0':
                    i += 1
        return count
                