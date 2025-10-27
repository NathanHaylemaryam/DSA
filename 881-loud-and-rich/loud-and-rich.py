import sys
sys.setrecursionlimit(10**6)
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)

        
        for a, b in richer:
            graph[b].append(a)

        ans = [-1] * n  

        def dfs(x):
            
            if ans[x] != -1:
                return ans[x]

           
            ans[x] = x

      
            for r in graph[x]:
                candidate = dfs(r)
                if quiet[candidate] < quiet[ans[x]]:
                    ans[x] = candidate

            return ans[x]

        for i in range(n):
            dfs(i)

        return ans