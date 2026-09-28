# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        count = 0
        dic = {}
        while current is not None:
            if current in dic and dic[current] != -1:
                return True
            dic[current] = count
            current = current.next
            count+=1
        return False

            

        