class BrowserHistory:

    def __init__(self, homepage: str):
        self.historyb = []
        self.historyf = []
        self.curr = homepage
        
    def visit(self, url: str) -> None:
        self.historyf = []
        self.historyb.append(self.curr)
        self.curr = url

    def back(self, steps: int) -> str:
        if steps > len(self.historyb):
            steps = len(self.historyb)
        if self.historyb:
            self.historyf.append(self.curr)
            for i in range(steps-1):
                self.historyf.append(self.historyb.pop())
            self.curr = self.historyb.pop()
        return self.curr

    def forward(self, steps: int) -> str:
        if steps > len(self.historyf):
            steps = len(self.historyf)
        if self.historyf:
            self.historyb.append(self.curr)
            for i in range(steps-1):
                self.historyb.append(self.historyf.pop())
            self.curr = self.historyf.pop()
        return self.curr


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)