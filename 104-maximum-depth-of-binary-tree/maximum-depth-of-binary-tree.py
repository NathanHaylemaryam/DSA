# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0

        cnt = 0
        if not root:
            return 0
        def move(root):
            
            nonlocal cnt , ans
            if root:
                
                cnt += 1
                ans = max(ans, cnt)
                move(root.left)
                move(root.right)
            
                cnt -= 1 
            
            
               
           
            
        move( root)

        return ans

