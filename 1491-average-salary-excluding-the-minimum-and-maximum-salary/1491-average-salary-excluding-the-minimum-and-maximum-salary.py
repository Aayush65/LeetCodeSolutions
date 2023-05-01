class Solution:
    def average(self, salary: List[int]) -> float:
        maxSal = 0
        minSal = salary[0]
        total = 0
        for i in salary:
            if minSal > i:
                minSal = i
            if maxSal < i:
                maxSal = i
            total += i
        avg = (total - minSal - maxSal) / (len(salary) - 2)
        return avg