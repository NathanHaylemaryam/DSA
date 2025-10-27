class DSU:
    def __init__(self, N):
        self.parent = list(range(N))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

class Solution:
    def regionsBySlashes(self, grid):
        n = len(grid)
        dsu = DSU(4 * n * n)

        for r in range(n):
            for c in range(n):
                root = 4 * (r * n + c)
                char = grid[r][c]

                
                if char == '/':
                    dsu.union(root + 0, root + 3)
                    dsu.union(root + 1, root + 2)
                elif char == '\\':
                    dsu.union(root + 0, root + 1)
                    dsu.union(root + 2, root + 3)
                else:  
                    dsu.union(root + 0, root + 1)
                    dsu.union(root + 1, root + 2)
                    dsu.union(root + 2, root + 3)


                if r + 1 < n:
                    dsu.union(root + 2, (root + 4 * n) + 0)
                if c + 1 < n:
                    dsu.union(root + 1, (root + 4) + 3)

    
        regions = len({dsu.find(x) for x in range(4 * n * n)})
        return regions
