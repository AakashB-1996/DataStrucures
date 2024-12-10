# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        result = head
        if not head:
            return result
        while head.next:
            if head.val != head.next.val:
                head = head.next
            else:
                head.next = head.next.next
        
        return result
