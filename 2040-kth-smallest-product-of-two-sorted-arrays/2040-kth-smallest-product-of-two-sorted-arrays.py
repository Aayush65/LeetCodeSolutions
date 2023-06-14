class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        posN1, negN1 = [i for i in nums1 if i >= 0], [-i for i in nums1 if i < 0][::-1]
        posN2, negN2 = [i for i in nums2 if i >= 0], [-i for i in nums2 if i < 0][::-1]

        def check(A: list[int], B: list[int], val: int) -> int:
            lessThans = 0
            j = len(B) - 1
            for i in range(len(A)):
                while j + 1 and A[i] * B[j] > val:
                    j -= 1
                lessThans += j + 1
            return lessThans


        negatives = len(posN1) * len(negN2) + len(posN2) * len(negN1)
        if k > negatives:
            k -= negatives
            sign = 1
        else:
            k = negatives - k + 1
            posN2, negN2 = negN2, posN2
            sign = -1


        lo, hi = 0, int(1e10)
        while lo < hi:
            mid = (lo + hi) // 2
            if check(posN1, posN2, mid) + check(negN1, negN2, mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return sign * lo