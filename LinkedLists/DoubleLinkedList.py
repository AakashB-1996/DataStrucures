class LinkedNode:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.left = LinkedNode(0)
        self.right = LinkedNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and curr != self.right and index == 0:
            return curr.val
        
        return -1
        

    def addAtHead(self, val: int) -> None:
        node,prev,next = ListNode(val),self.left,self.left.next
        node.next = next
        next.prev = node
        node.prev = prev
        prev.next = node
        
        

    def addAtTail(self, val: int) -> None:
        node,prev,next = ListNode(val),self.right.prev,self.right
        node.next = next
        next.prev = node
        node.prev = prev
        prev.next = node
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and index == 0:
            node,next,prev = ListNode(val),curr,curr.prev
            node.next = next
            next.prev = node
            node.prev = prev
            prev.next = node

        
        

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and curr != self.right and index == 0:
            next,prev = curr.next,curr.prev
            prev.next = next
            next.prev = prev
