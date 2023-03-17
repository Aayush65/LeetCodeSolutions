class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        letters = {'c':0,'r':1,'o':2,'a':3,'k':4}
        hm = [0] * 5
        frogs = 0
        for i in croakOfFrogs:
            hm[letters[i]] += 1
            if letters[i] and hm[letters[i] - 1] < hm[letters[i]]:
                return -1
            frogs = max(frogs, hm[0] - hm[-1])
        
        for i in hm:
            if i != hm[0]:
                return -1
        return frogs