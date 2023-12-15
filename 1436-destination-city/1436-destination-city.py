class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        ways = set()
        noways = set()
        
        for i in paths:
            ways.add(i[0])
            if i[0] in noways:
                noways.remove(i[0])
            if i[1] not in ways:
                noways.add(i[1])
            
        noway = list(noways)
        return noway[-1]