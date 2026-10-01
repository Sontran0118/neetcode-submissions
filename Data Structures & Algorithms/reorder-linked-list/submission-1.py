# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node = []
        current = head
        while current is not None:
            node.append(current)
            current = current.next
        i = 0
        j = len(node) - 1
        while i < j:
            node[i].next = node[j]
            i+=1
            if i>=j:
                break
            node[j].next = node[i]
            j-=1
        node[i].next = None
       
        