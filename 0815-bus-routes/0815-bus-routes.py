class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        nodeRoutes = defaultdict(set)
        for route in range(len(routes)):
            for i in routes[route]:
                nodeRoutes[i].add(route)
        routes = [set(i) for i in routes]

        stops = {source}
        buses = 0
        visited = {source}
        visitedRoutes = set()
        while stops:
            newStops = set()
            for stop in stops:
                if stop == target:
                    return buses
                for route in nodeRoutes[stop]:
                    if route in visitedRoutes:
                        continue
                    visitedRoutes.add(route)
                    for nextStop in routes[route]:
                        if nextStop in visited:
                            continue
                        visited.add(nextStop)
                        newStops.add(nextStop)
            stops = newStops
            buses += 1
        return -1