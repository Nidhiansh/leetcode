# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        res=[]
        inorder(root)
        i=0
        j=len(res)-1
        while i<j:
            if res[i]+res[j]==k:
                return True
            elif res[i]+res[j]>k:
                j-=1
            elif res[i]+res[j]<k:
                i+=1
        return False