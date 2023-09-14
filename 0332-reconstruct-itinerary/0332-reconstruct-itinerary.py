class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from sortedcontainers import SortedList
        
        destMap = {i[0]: SortedList() for i in tickets}
        for i, j in tickets:
            destMap[i].add(j)
        
        path = ["JFK"]
        
        def dfs(city: str) -> bool:
            if len(path) == len(tickets) + 1:
                return True
            if city not in destMap or not destMap[city]:
                return False                

            for i in range(len(destMap[city])):
                nextCity = destMap[city][i]
                destMap[city].pop(i)
                path.append(nextCity)
                if dfs(nextCity):
                    return True
                path.pop()
                destMap[city].add(nextCity)
            return False

        dfs("JFK")
        return path