class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        #   q1  p1
        #   i/j
        # 2  3  4
        # 1  3  5
        # i     
        #  p2/q2
        if not num1:
            n = len(num2)//2
            return (num2[n] + num2[-n -1])/2
        if not num2:
            n = len(num1)//2
            return (num1[n] + num1[-n -1])/2
        p1 = p2 = 0
        q1 = q2 = -1
        i = -inf
        j = inf
        while i < j:        
            if p2 >= len(num2) or p1 < len(num1) and num1[p1] <= num2[p2]:
                i = num1[p1]
                p1 += 1
            else:
                i = num2[p2]
                p2 += 1
            if not i > j:
                if q2 < -len(num2) or q1 >= -len(num1) and num1[q1] >= num2[q2] :
                    j = num1[q1]
                    q1 -= 1
                else:
                    j = num2[q2]
                    q2 -= 1
        return (i+j)/2