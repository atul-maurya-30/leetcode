# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def hcf(self,a,b):
        if b==0:
            return a
        else:
            return self.hcf(b,a%b)
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=head #t is used for traversing the linkedlist
        while t.next: #loop continues as lomg as t has next node
            n=ListNode(gcd(t.val,t.next.val)) #calculating gcd
            n.next=t.next #new node next is set to the original next
            t.next=n #next pointer is updated to point to the new node
            t=t.next.next #current node move two steps forward
        return head #print the new linked list