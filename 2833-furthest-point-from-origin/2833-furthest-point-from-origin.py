class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        l=0
        r=0
        n=len(moves)
        for i in moves:
            if i=="L":
                l+=1
            elif i=="R":
                r+=1
        return n-(l+r)+abs(l-r)