class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        u={}
        l={}
        for idx,i in enumerate(word):
            if i.islower():
                l[i]=idx
            if i.isupper() and i not in u:
                u[i]=idx
        c=0
        for i in u:
            if i.lower() in l and i in u:
                if l[i.lower()]<u[i]:
                    c+=1
        return c