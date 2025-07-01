# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def move(root):
            if root:
                move(root.left)
                arr.append(root.val)
                move(root.right)
        move(root)
        print(arr)
        def build(arr):
            if not arr:
                return None
            mid = len(arr) //2
            root = TreeNode(arr[mid])
            root.left = build(arr[:mid])
            root.right = build(arr[mid+1:])
            return root
        return build(arr)



