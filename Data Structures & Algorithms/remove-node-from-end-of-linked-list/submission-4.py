# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = []
        current = head
        while current:
            node.append(current)
            current = current.next
        if n > len(node):
            return None
        if n == 0:
            return head
        if n == len(node):
            head = head.next
            return head
        node[len(node)-n-1].next = node[len(node)-n].next
        return head
            
        