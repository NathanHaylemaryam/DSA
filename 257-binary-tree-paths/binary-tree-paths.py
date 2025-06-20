# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []
        temp = []
        def move(root):
            nonlocal path , temp
            if not root:
                return
            
            temp.append(str(root.val))
            if not root.left and not root.right:
                path.append('->'.join(temp))
            else:
                move(root.left)
                move(root.right)
            temp.pop()
        move(root)
        return path