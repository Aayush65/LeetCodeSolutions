class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        org = 0        
        for i in range(n - 1):
            org = derived[i] ^ org           
        
        if org ^ derived[-1] == 0:
            return True
        return False