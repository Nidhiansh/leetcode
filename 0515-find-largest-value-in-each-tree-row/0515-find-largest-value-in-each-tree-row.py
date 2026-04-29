# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        q=deque()
        q.append(root)
        res=[]
        while q:
            temp=float("-inf")
            for _ in range(len(q)):
                fro=q.popleft()
                temp=max(temp,fro.val)
                if fro.left:
                    q.append(fro.left)
                if fro.right:
                    q.append(fro.right)
            res.append(temp)
        return res