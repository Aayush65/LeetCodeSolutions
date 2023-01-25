class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        distMap = {}
        i = node1
        dist = 0
        while i != -1:
            if i in distMap:
                break
            distMap[i] = dist
            i = edges[i]
            dist += 1

        i = node2
        dist = 0
        visited = set()
        closestNode = -1
        minDist = float("inf")
        while i != -1:
            if i in visited:
                break
            visited.add(i)
            if i in distMap:
                if minDist > max(dist, distMap[i]):
                    minDist = max(dist, distMap[i])
                    closestNode = i
                elif minDist == max(dist, distMap[i]):
                    closestNode = min(closestNode, i)
            dist += 1
            i = edges[i]
        return closestNode