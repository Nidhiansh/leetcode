class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        total=sum(matchsticks)
        if total%4!=0:
            return False
        target=total//4
        matchsticks.sort(reverse=True)
        if matchsticks[0]>target:
            return False
        sides=[0]*4
        n=len(matchsticks)
        def dfs(idx):
            if idx==n:
                return sides[0]==sides[1]==sides[2]==target
            for i in range(4):
                if sides[i]+matchsticks[idx]<=target:
                    sides[i]+=matchsticks[idx]
                    if dfs(idx+1):
                        return True
                    sides[i]-=matchsticks[idx]
                if sides[i]==0:
                    break
            return False  
        return dfs(0)