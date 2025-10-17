class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def bfs(start):
            q = deque([start])
            visited[start] = True
            nodes = {start}
            edges_count = 0

            while q:
                node = q.popleft()
                for nei in graph[node]:
                    edges_count += 1
                    if not visited[nei]:
                        visited[nei] = True
                        nodes.add(nei)
                        q.append(nei)
            edges_count //= 2
            return nodes, edges_count

        complete_count = 0

        for i in range(n):
            if not visited[i]:
                nodes, edges_count = bfs(i)
                k = len(nodes)
                if edges_count == k * (k - 1) // 2:
                    complete_count += 1

        return complete_count