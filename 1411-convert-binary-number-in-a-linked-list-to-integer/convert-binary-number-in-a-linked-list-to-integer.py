# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        s = []
        while head:
            s.append(str(head.val))
            head= head.next


        b = ''.join(s)
        b = int(b)
        res = 0 
        i = 0
        print(b)
        while b > 0:
            temp = b % 10
            res += (2**i)*temp
            i += 1
            b //= 10
        return res