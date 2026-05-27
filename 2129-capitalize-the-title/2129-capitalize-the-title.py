class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        l=title.split()
        for i,w in enumerate(l):
            if len(w)<3:
                l[i]=w.lower()
            else:
                l[i]=w[0].upper()+w[1:].lower()
        return " ".join(l)