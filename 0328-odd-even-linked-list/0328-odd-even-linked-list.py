# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: #if emoty
            return None
        
        curr1=ListNode() #initialize dummy node for odd list
        curr2=ListNode() #initialize dummy node for even list
        odd=curr1 #pointer for odd list
        even=curr2 #pointer for even list

#pointers used for linking the nodes of even as well as odd
        i=1
        while head!=None:
            if i%2!=0: #for odd 
                odd.next=head
                odd=odd.next

            else: #for even
                even.next=head
                even=even.next

            head=head.next
            i+=1
            
        #terminate even list
        even.next=None

        #add the even list to the end of odd list
        odd.next=curr2.next

        return curr1.next
