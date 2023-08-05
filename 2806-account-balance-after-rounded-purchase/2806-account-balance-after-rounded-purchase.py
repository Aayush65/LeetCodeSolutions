class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        diff = purchaseAmount % 10
        if diff >= 5:
            purchaseAmount = purchaseAmount - diff + 10
        else:
            purchaseAmount -= diff
        return 100 - purchaseAmount