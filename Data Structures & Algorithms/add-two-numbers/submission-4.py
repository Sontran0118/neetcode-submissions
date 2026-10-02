# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        cur1 = l1
        cur2 = l2
        remaining = 0
        root = None
        sum_node = 0
        while True:
            if cur1 and cur2:
                sum_node = cur1.val+cur2.val + remaining
            elif not cur1:
                sum_node = cur2.val+remaining
            elif not cur2:
                sum_node = cur1.val+remaining
            node = ListNode((sum_node)%10)
            remaining = sum_node // 10
            if prev:
                prev.next = node
            else:
                root = node
            prev = node    
            if cur1: cur1 = cur1.next
            if cur2: cur2 = cur2.next
            if not cur1 and not cur2:
                if remaining >0:
                    prev.next = ListNode(remaining) 
                
                break
           
        return root
        