# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        temp  = 0 
        found = False
        def move(root, target):
            nonlocal temp, found

            if root:
                temp += root.val
                if (not root.left ) and  (not root.right):
                    if temp == target:
                        found = True
                move(root.left, target)
                move(root.right, target)
                temp -= root.val   
        move(root, targetSum)
        return found

        