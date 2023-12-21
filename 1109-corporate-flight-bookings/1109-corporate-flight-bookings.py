class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flights = [0] * (n + 1)
        for left, right, seats in bookings:
            flights[left - 1] += seats
            flights[right] -= seats
        total = 0
        for i in range(n):
            total += flights[i]
            flights[i] = total
        flights.pop()
        return flights