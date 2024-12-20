# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #dfs function for helper function
        def dfs(n1,n2,l):
            #stop recursion if any node is None
            if not n1 or not n2:
                return

            #swap values if current level is odd
            if l%2!=0:
                n1.val,n2.val=n2.val,n1.val

            #recursive call to left of n1 and right of n2(working like mirror image nodes)
            dfs(n1.left,n2.right,l+1)
            #recursive call to right of n1 and left of n2 (other pairs of mirror nodes).
            dfs(n1.right,n2.left,l+1)

        #start dfs with left and right children of the root node at level 1
        dfs(root.left,root.right,1)

        #return the updated tree
        return root