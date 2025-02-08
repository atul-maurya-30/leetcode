# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res=[]

        def preorder(node):
            if not node:
                return 
            preorder(node.left) #visit left subtree
            res.append(node.val) #visit root first
            preorder(node.right) #visit right subtree
        
        preorder(root) #start preorder traversal
        s=0
        for i in res:
            if low<=i<=high:
                s+=i
        return s