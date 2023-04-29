class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        hs1 = set()
        hs2 = set()
        hs = set()
        C = []
        for i in range(len(A)):
            hs1.add(A[i])
            hs2.add(B[i])
            if A[i] in hs2:
                hs.add(A[i])
            if B[i] in hs1:
                hs.add(B[i])
            C.append(len(hs))
        return C