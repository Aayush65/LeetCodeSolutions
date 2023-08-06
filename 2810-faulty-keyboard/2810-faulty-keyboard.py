class Solution:
    def finalString(self, s: str) -> str:
        newS = []
        for i in s:
            if i == 'i':
                newS.reverse()
            else:
                newS.append(i)
        return ''.join(newS)