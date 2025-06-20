# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        cnt =0 
        def move(node):
            nonlocal cnt
            if not node:
                return (0, 0) 

            left_sum, cnt_1 = move(node.left)
            right_sum, cnt_2 = move(node.right)

            total_s = node.val + left_sum + right_sum
            total_cnt = 1 + cnt_1 + cnt_2

            if node.val == total_s // total_cnt:
                cnt += 1

            return (total_s, total_cnt)

        move(root)
        return cnt