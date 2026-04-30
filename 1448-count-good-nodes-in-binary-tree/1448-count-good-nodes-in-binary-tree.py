# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.c=1
        def rec(node,prev_m):
            if not node:
                return
            if node.left:
                if node.left.val>=prev_m:
                    self.c+=1
                    rec(node.left,node.left.val)
                else:
                    rec(node.left,prev_m)
            if node.right:
                if node.right.val>=prev_m:
                    self.c+=1
                    rec(node.right,node.right.val)
                else:
                    rec(node.right,prev_m)
        rec(root,root.val)
        return self.c
