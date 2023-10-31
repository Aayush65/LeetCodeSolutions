class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        total = sum(milestones)
        maxi = max(milestones)
        
        return total if total >= 2 * maxi else 2 * (total - maxi) + 1