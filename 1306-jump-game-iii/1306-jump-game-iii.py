class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
    
        visited = set()    
        def dfs(index: int) -> bool:
            if not -1 < index < len(arr):
                return False
            if index in visited:
                return False
            visited.add(index)
            if arr[index] == 0:
                return True
            res = dfs(arr[index] + index) or dfs(index - arr[index])
            return res
        
        return dfs(start)