class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        def extractContent(f: int) -> int:
            for i in range(len(f)):
                if f[i] == '(':
                    return [f[:i], f[i + 1: len(f) - 1]]                
        
        fileLoc = defaultdict(list)
        for path in paths:
            path = path.split()
            loc = path[0]
            for i in path:
                if i == loc:
                    continue
                name, content = extractContent(i)
                fileLoc[content].append(loc + '/' + name)
        
        res = []
        for i in fileLoc:
            if len(fileLoc[i]) > 1:
                res.append(fileLoc[i])
        return res
            
        