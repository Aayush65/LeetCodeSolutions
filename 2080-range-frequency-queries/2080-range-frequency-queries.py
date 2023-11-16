class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.freq = {i: [] for i in arr}
        for i, x in enumerate(arr):
            self.freq[x].append(i)
    
    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.freq:
            return 0
        lIdx = bisect_left(self.freq[value], left)
        rIdx = bisect_right(self.freq[value], right)
        return rIdx - lIdx

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)