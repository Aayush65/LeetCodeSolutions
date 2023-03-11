class Solution:
        def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
            ab = lcm(a, b)
            bc = lcm(b, c)
            ac = lcm(a, c)
            abc = lcm(a, b, c)

            def check(val: int) -> bool:
                na = val // a
                nb = val // b
                nc = val // c
                nab = val // ab
                nbc = val // bc
                nac = val // ac
                nabc = val // abc
                rank = na + nb + nc - nab - nbc - nac + nabc
                return rank >= n

            lo = n
            hi = n * abc
            while lo < hi:
                mid = (lo + hi) // 2
                if check(mid):
                    hi = mid
                else:
                    lo = mid + 1
            return lo