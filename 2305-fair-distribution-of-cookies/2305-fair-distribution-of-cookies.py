class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bags = [0]*k
        def distribution(index: int) -> int:
            if index == len(cookies):
                return max(bags)
            res = float("inf")
            visited = set()
            for i in range(k):
                if bags[i] in visited:
                    continue
                visited.add(bags[i])
                bags[i] += cookies[index]
                res = min(res, distribution(index + 1))
                bags[i] -= cookies[index]
            return res
        return distribution(0)