class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        
        directions = {
            1: [(0, -1), (0, 1)],     
            2: [(-1, 0), (1, 0)],     
            3: [(0, -1), (1, 0)],     
            4: [(0, 1), (1, 0)],      
            5: [(0, -1), (-1, 0)],    
            6: [(0, 1), (-1, 0)],     
        }

        opposite = {
            (0, 1): (0, -1),
            (0, -1): (0, 1),
            (1, 0): (-1, 0),
            (-1, 0): (1, 0)
        }

        visited = [[False] * n for _ in range(m)]
        q = deque([(0, 0)])
        visited[0][0] = True

        while q:
            i, j = q.popleft()
            if (i, j) == (m - 1, n - 1):
                return True

            for dx, dy in directions[grid[i][j]]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
               
                    if opposite[(dx, dy)] in directions[grid[ni][nj]]:
                        visited[ni][nj] = True
                        q.append((ni, nj))

        return False