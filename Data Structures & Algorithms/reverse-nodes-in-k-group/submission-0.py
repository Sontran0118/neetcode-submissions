# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next





class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
           return head

        node_arr = []
        current = head

        while current:
            node_arr.append(current)
            current = current.next

        dummy = ListNode(0)
        current = dummy

        for i in range(0, len(node_arr), k):
            group = node_arr[i:i + k]

            if len(group) == k:
                group.reverse()

            for node in group:
                current.next = node
                current = current.next

        current.next = None
        return dummy.next


        
    

        