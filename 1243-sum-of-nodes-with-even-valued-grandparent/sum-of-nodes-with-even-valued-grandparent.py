# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        even = 0
        def move(root):
            nonlocal even
            if root:
                if root.val % 2 == 0:
                    if root.left:
                            if root.left.left:
                                even += root.left.left.val
                            if root.left.right:
                                even += root.left.right.val
                    if root.right:
                        if root.right.left:
                            even += root.right.left.val
                        if root.right.right:
                            even += root.right.right.val 
                move(root.left)
                move(root.right)
        move(root)
        return even


        