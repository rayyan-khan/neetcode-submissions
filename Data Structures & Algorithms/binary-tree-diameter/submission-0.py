# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            leftHeight = self.maxHeight(root.left)
            rightHeight = self.maxHeight(root.right)
            diameter = leftHeight + rightHeight
            diam = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
            return max(diameter, diam)
            

    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1+max(self.maxHeight(root.left), self.maxHeight(root.right))
        