class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack=[]
        if len(num)<=k:
            return "0"
        for i in num:
            while k>0 and stack and stack[-1]>i:
                stack.pop()
                k-=1
            stack.append(i)
        if k>0:
            stack=stack[:-k]
        return "".join(stack).lstrip("0")or "0"