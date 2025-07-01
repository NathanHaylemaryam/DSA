# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pre = 0
        def move(root):
            nonlocal pre
            if root:
                move(root.right)
                root.val += pre
                pre = root.val
                move(root.left)
        move(root)
        return root

        