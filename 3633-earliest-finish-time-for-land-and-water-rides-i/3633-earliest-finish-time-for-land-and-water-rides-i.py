class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        # res=float('inf')
        # n=len(landStartTime)
        # m=len(waterStartTime)
        # for i in range(n):
        #     t1=landStartTime[i]+landDuration[i]
        #     for j in range(m):
        #         t2=max(t1,waterStartTime[j])+waterDuration[j]
        #         res=min(res,t2)
        # for i in range(m):
        #     t1=waterStartTime[i]+waterDuration[i]
        #     for j in range(n):
        #         t2=max(t1,landStartTime[j])+landDuration[j]
        #         res=min(res,t2)
        # return res
        def func(a,ad,b,bd):
            m=float('inf')
            for i in range(len(a)):
                m=min(m,a[i]+ad[i])
            res=float('inf')
            for i in range(len(b)):
                res=min(res,max(b[i],m)+bd[i])
            return res
        return min(func(landStartTime,landDuration,waterStartTime,waterDuration),func(waterStartTime,waterDuration,landStartTime,landDuration))