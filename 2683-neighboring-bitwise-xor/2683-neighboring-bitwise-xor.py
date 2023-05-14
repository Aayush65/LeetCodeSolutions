class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        org = [0]        
        for i in range(n - 1):
            org.append(derived[i] ^ org[-1])            
        
        if org[-1] ^ derived[-1] == org[0]:
            return True
        return False