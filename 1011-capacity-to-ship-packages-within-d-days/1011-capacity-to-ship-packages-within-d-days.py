class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(capacity):
            count = 1
            current = 0
            for weight in weights:
                current += weight
                if current > capacity:
                    count += 1
                    current = weight
                    if count > days:
                        return days + 1
            return count
        left, right = max(weights), sum(weights)
        if days == len(weights):
            return left
        while left < right:
            mid = (left + right) // 2
            if check(mid) > days:
                left = mid + 1
            else:
                right = mid
        return right

            