# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr=None,head
        while curr:
            curr.next,prev,curr=prev,curr,curr.next
            '''nxt=curr.next# as if we do not link the next nodes to temporary node then it will be lost so that this line we have to used
            curr.next=prev#now we have the next node address into previous node
            prev=curr#we have to now move on the nodes forward
            curr=nxt#we have to move on forward'''
            
        return prev