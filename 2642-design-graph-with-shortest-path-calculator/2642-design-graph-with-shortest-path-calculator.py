class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.nodeMap = {i: set() for i in range(n)}
        for i, j, w in edges:
            self.nodeMap[i].add((j, w))
        
    def addEdge(self, edge: List[int]) -> None:
        self.nodeMap[edge[0]].add((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        h = [(0, node1)]
        visited = set()
        while h:
            cost, node = heappop(h)
            if node == node2:
                return cost
            if node in visited:
                continue
            visited.add(node)
            for nei, weight in self.nodeMap[node]:
                heappush(h, [cost + weight, nei])
        return -1
        
# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)