# class Node:
#     def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
#         self.val = val
#         self.isLeaf = isLeaf
#         self.topLeft = topLeft
#         self.topRight = topRight
#         self.bottomLeft = bottomLeft
#         self.bottomRight = bottomRight

class Solution:
    def construct(self, grid):
        def build(x, y, size):
            val = grid[x][y]
            isLeaf = True
            for i in range(x, x + size):
                for j in range(y, y + size):
                    if grid[i][j] != val:
                        isLeaf = False
                        break
                if not isLeaf:
                    break
            if isLeaf:
                return Node(val=val, isLeaf=True)
            else:
                mid = size // 2
                return Node(
                    val=False,
                    isLeaf=False,
                    topLeft=build(x, y, mid),
                    topRight=build(x, y + mid, mid),
                    bottomLeft=build(x + mid, y, mid),
                    bottomRight=build(x + mid, y + mid, mid)
                )
        
        n = len(grid)
        return build(0, 0, n)
