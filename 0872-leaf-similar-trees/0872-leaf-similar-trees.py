# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root):#helper function
            if root is None: #current node is none,return empty list
                return []
            #if current node is a leaf node, return its value in a list
            if root.left is None and root.right is None:
                return [root.val] #we have to compared two new list 
            return dfs(root.left)+dfs(root.right) #get leaf values from right and left subtrees
            
        return dfs(root1)==dfs(root2) #compare