# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #simple iterative approach
        if not head or not head.next: #empty or has only one node
            return None
        
        #count and current initalised
        c=0
        curr=head

        #loop until curr empty
        while curr:
            c+=1 #increment count
            curr=curr.next #next node
        m=c//2 #mid value index for deletion

        curr=head #again intialise from head
        i=0 #iterations
        prev=ListNode() #initialise linkedlist class

        while i<m: #loop until it iterations reach mid value
            i+=1 #increment iteration by 1
    
            prev=curr #keep track of previous node
            curr=curr.next # move to next node
        prev.next=curr.next #skip middle node by connecting prev node to next of the current node

        return head #return linked list