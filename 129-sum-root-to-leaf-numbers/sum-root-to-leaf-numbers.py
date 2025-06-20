# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        path = []
        temp = []
        def move(root):
            nonlocal path, temp
            if not root:
                return 0
            temp.append(str(root.val))
            if not root.left and not root.right:
                path.append(int(''.join(temp)))
            else:
                move(root.left)
                move(root.right)
            temp.pop()
        move(root)
        return sum(path)