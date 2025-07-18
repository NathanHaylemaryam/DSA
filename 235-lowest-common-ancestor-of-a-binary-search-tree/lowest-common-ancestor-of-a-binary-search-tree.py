# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def move(root, p , q):
            if root:
                if root.val > p.val and root.val > q.val:
                    return move(root.left ,p , q)
                elif root.val < p.val and root.val < q.val:
                    return move(root.right, p , q)
                else:
                    return root
        return move(root, p , q)
        