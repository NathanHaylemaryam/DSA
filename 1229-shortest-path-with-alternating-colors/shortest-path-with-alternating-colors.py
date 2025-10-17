class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)
        for u, v in redEdges:
            red_graph[u].append(v)
        for u, v in blueEdges:
            blue_graph[u].append(v)

        res = [-1] * n
        q = deque([(0, 0), (0, 1)])  # (node, color) 0=red, 1=blue
        visited = {(0, 0), (0, 1)}
        dist = 0

        while q:
            for _ in range(len(q)):
                node, color = q.popleft()
                if res[node] == -1:
                    res[node] = dist
                if color == 0:
                    for nei in blue_graph[node]:
                        if (nei, 1) not in visited:
                            visited.add((nei, 1))
                            q.append((nei, 1))
                else:
                    for nei in red_graph[node]:
                        if (nei, 0) not in visited:
                            visited.add((nei, 0))
                            q.append((nei, 0))
            dist += 1
        return res