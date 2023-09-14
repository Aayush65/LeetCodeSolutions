class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from sortedcontainers import SortedList
        
        destMap = {i[0]: SortedList() for i in tickets}
        for i, j in tickets:
            destMap[i].add(j)
        
        itenerary = []
        
        def dfs(city: str, path: list[str]) -> bool:
            if city not in destMap or not destMap[city]:
                if len(path) != len(tickets) + 1:
                    return False
                nonlocal itenerary
                itenerary = path
                return True

            for i in range(len(destMap[city])):
                nextCity = destMap[city][i]
                destMap[city].pop(i)
                path.append(nextCity)
                if dfs(nextCity, path):
                    return True
                path.pop()
                destMap[city].add(nextCity)
            return False

        dfs("JFK", ["JFK"])
        return itenerary