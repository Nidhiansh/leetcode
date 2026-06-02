class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        res=float('inf')
        n=len(landStartTime)
        m=len(waterStartTime)
        for i in range(n):
            t1=landStartTime[i]+landDuration[i]
            for j in range(m):
                t2=max(t1,waterStartTime[j])+waterDuration[j]
                res=min(res,t2)
        for i in range(m):
            t1=waterStartTime[i]+waterDuration[i]
            for j in range(n):
                t2=max(t1,landStartTime[j])+landDuration[j]
                res=min(res,t2)
        return res