# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt  = 0
        def check(node, currentSum):
            nonlocal cnt
            if not node:
                return
            currentSum += node.val
            if currentSum == targetSum:
                cnt += 1
            check(node.left, currentSum)
            check(node.right, currentSum)

        def move(node):
            if not node:
                return
            check(node, 0)
            move(node.left)
            move(node.right)

        move(root)
        return cnt
