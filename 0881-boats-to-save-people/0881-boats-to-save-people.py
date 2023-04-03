class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        n = len(people)
        i, j = 0, n - 1
        while i <= j:
            if i == j or people[i] + people[j] <= limit:
                i += 1
            j -= 1                    
            boats += 1
        return boats