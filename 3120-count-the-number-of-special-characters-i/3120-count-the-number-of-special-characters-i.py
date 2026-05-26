class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        l=set()
        u=set()
        for i in word:
            if i.islower():
                l.add(i)
            else:
                u.add(i)
        c=0
        for i in l:
            if i.upper() in u:
                c+=1
        return c