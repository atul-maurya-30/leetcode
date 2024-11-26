# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head.next #skip initial zero
        new_head=ListNode(0) #pointer to build new list
        new_tail=new_head 

        #to store the sum betweeen zeros
        s=0

        while curr:
            if curr.val==0:
                #create a new node with sum when encountering zeros
                new_tail.next=ListNode(s)
                new_tail=new_tail.next
                s=0 #reset the sum for the next gap
            else:
                #add current node's value to the sum
                s+=curr.val
            curr =curr.next #move to the next node
        return new_head.next #return the merged list(skiping first dummy node)
