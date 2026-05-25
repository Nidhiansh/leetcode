class Solution(object):
    def passwordStrength(self, password):
        """
        :type password: str
        :rtype: int
        """
        l=set()
        u=set()
        d=set()
        s=set()
        for i in password:
            if i.islower():
                l.add(i)
            elif i.isupper():
                u.add(i)
            elif i.isdigit():
                d.add(i)
            elif i=="!" or i=="@" or i=="#" or i=="$":
                s.add(i)
        return 1*len(l)+2*len(u)+3*len(d)+5*len(s)