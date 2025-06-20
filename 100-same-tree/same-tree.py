# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        found = True
        def move(p , q):
            nonlocal found
            if not p and not q:
                return
            if not p or not q:
                found = False
                return
            if p and q:
                if p.val != q.val:
                    found =  False
                
                move(p.left, q.left)
                move(p.right , q.right)
        move(p , q)
        return found
        