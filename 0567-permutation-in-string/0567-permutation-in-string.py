class Solution:
    def checkInclusion(self, s2: str, s1: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n2 > n1:
            return False

        s2Map = {i: 0 for i in s2}
        for i in s2:
            s2Map[i] += 1

        def op(val: int, toAdd: int) -> None:
            if val in s2Map:
                s2Map[val] += toAdd
                if not s2Map[val]:
                    del s2Map[val]
            else:
                s2Map[val] = toAdd
        
        for i in range(n2):
            op(s1[i], -1)


        for i in range(n2, n1):
            if not s2Map:
                return True
            op(s1[i], -1)
            op(s1[i - n2], 1)

        return not len(s2Map)