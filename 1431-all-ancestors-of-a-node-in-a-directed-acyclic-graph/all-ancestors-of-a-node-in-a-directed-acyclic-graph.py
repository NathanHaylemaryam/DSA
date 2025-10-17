class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        ancestors = [set() for _ in range(n)]
        q = deque([i for i in range(n) if indegree[i] == 0])

        while q:
            node = q.popleft()
            for nei in graph[node]:
                ancestors[nei].add(node)
                ancestors[nei].update(ancestors[node])
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return [sorted(list(a)) for a in ancestors]