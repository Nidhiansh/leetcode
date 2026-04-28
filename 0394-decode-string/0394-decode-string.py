class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        t=""
        n=0
        for i in s:
            if i.isdigit():
                n=n*10+int(i)
            elif i=="[":
                stack.append((t,n))
                t=""
                n=0
            elif i=="]":
                p,num=stack.pop()
                t=p+num*t
            else:
                t+=i
        return t