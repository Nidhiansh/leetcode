# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def greater(node):
            if not node:
                return
            greater(node.right)
            self.temp+=node.val
            node.val=self.temp
            greater(node.left)
        self.temp=0
        greater(root)
        return root