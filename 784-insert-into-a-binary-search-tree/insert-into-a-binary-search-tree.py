# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def find(root , val):
            if not root:
                return TreeNode(val)
            elif root.val > val:
                root.left = find(root.left , val)
            else:
                root.right = find(root.right , val)
            return root
        return find(root, val)

            