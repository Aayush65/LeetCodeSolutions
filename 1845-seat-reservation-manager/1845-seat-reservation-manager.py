class SeatManager:

    def __init__(self, n: int):
        self.unreserved = [i for i in range(1, n + 1)]
        self.reserved = set()

    def reserve(self) -> int:
        while self.unreserved[0] in self.reserved:
            heappop(self.unreserved)
        newSeat = heappop(self.unreserved)
        self.reserved.add(newSeat)
        return newSeat

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.unreserved, seatNumber)
        self.reserved.remove(seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)