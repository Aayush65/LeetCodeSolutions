class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        newS = []
        i = 0
        while i < len(s):
            if s[i] == ')':
                if i == len(s) - 1 or s[i + 1] != ')':
                    insertions += 1
                    i += 1
                else:
                    i += 2
                newS.append(')')
            else:
                newS.append('(')
                i += 1
        s = ''.join(newS)
        # print(s)
        
        open = 0
        for i in s:
            if i == ')':
                if not open:
                    insertions += 1
                else:
                    open -= 1
            else:
                open += 1
        return insertions + open * 2
                