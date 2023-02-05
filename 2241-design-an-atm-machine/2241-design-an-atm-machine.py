class ATM:

    def __init__(self):
        # [20, 50, 100, 200, 500]
        self.cash = [0, 0, 0, 0, 0]
        self.val = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.cash[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> list[int]:
        tempCash = self.cash.copy()
        res = [0, 0, 0, 0, 0]
        for i in range(4, -1, -1):
            if self.cash[i] > 0:
                notes = 0
                if amount // self.val[i] <= self.cash[i]:
                    notes = amount // self.val[i]
                else:
                    notes = self.cash[i]
                self.cash[i] -= notes
                amount -= notes * self.val[i]
                res[i] += notes
            if amount == 0: 
                return res
        self.cash = tempCash
        return [-1]

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)