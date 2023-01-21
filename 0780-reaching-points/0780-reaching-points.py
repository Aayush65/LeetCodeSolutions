class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx + ty or ty >= sy + tx:
            if tx > ty:
                tx = sx + (tx - sx) % ty
            else:
                ty = sy + (ty - sy) % tx
        return tx == sx and ty == sy