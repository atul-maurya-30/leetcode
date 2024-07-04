# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        #we use floyd's cylcle-finding algortihm, also known as the Tortoise and hare alo
#it uses two pointers,moving at different speeds,to traverse the sequence
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False