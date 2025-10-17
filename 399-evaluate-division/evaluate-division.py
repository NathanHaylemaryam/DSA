class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
    
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val
        
        def dfs(start, end, visited):
            if start not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            for nei, val in graph[start].items():
                if nei in visited:
                    continue
                res = dfs(nei, end, visited)
                if res != -1.0:
                    return val * res
            return -1.0
        
        return [dfs(c, d, set()) for c, d in queries]