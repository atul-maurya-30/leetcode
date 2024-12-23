# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minswaps(self,temp):
        #calculate minimum no. of swaps to sort the array "temp"
        s=0
        sorted_l=sorted(temp) #sort array
        h={v:u for u,v in enumerate(temp)} #map value to index

        for i in range(len(temp)):
            if temp[i]!=sorted_l[i]: #if value not in correct position
                curr=h[sorted_l[i]] #get correct index
                h[temp[i]]=curr #update map values
                temp[curr],temp[i]=temp[i],temp[curr] #swap values
                s+=1 #increment swap count
        return s

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        #perform bfs and calculate the total swaps needed for all levels
        q=deque([root]) #inititalise queue for bfs
        s=0

        while q:
            l=[] #store node values at current level
            for _ in range(len(q)):
                n=q.popleft() #pop the values
                l.append(n.val) #add values to level list

                #add left and right children to queue if they exist
                if n.left:
                    q.append(n.left) #add left child
                if n.right:
                    q.append(n.right) #add right child
            #calculate swaps required to sort the current level
            s+=self.minswaps(l)
        return s
