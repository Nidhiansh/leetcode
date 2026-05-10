class Solution(object):
    def scoreValidator(self, events):
        """
        :type events: List[str]
        :rtype: List[int]
        """
        counter=0
        score=0
        for i in events:
            if counter==10:
                break
            elif i=="W":
                counter+=1
            elif i=="WD" or i=="NB":
                score+=1
            else:
                score+=int(i)
        return [score,counter]