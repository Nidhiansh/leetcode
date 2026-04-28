class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for i in s:
            stack.append(i)
            if len(stack)>1:
                if stack[-1]==stack[-2]:
                    stack.pop()
                    stack.pop()
        return "".join(stack)