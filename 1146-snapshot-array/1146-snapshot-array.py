class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[] for i in range(length)]
        self.snapId = 0

    def set(self, index: int, val: int) -> None:
        if self.arr[index] and self.arr[index][-1][1] == self.snapId:
            self.arr[index][-1][0] = val
        else:
            self.arr[index].append([val, self.snapId])

    def snap(self) -> int:
        self.snapId += 1
        return self.snapId - 1

    def get(self, index: int, snap_id: int) -> int:
        idx = bisect_left(self.arr[index], snap_id, key = lambda x: x[1])
        if idx >= len(self.arr[index]):
            return self.arr[index][-1][0] if self.arr[index] else 0
        if self.arr[index][idx][1] != snap_id:
            idx -= 1
            return self.arr[index][idx][0] if idx != -1 else 0
        return self.arr[index][idx][0]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)