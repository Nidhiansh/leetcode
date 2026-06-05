class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def solve(n_str):
            if not n_str:return 0
            memo={}
            def dp(idx,prev,prev2,is_less,is_started):
                if idx==len(n_str):return (1,0) if is_started else (0,0)
                state=(idx,prev,prev2,is_less,is_started)
                if state in memo:return memo[state]
                limit=9 if is_less else int(n_str[idx])
                tot_cnt,tot_wav=0,0
                for d in range(limit+1):
                    ni_less=is_less or (d<limit)
                    if not is_started:
                        if d==0:
                            c,w=dp(idx+1,-1,-1,ni_less,False)
                            tot_cnt+=c;tot_wav+=w
                        else:
                            c,w=dp(idx+1,d,-1,ni_less,True)
                            tot_cnt+=c;tot_wav+=w
                    else:
                        n_wav=0
                        if prev2!=-1 and prev!=-1:
                            if prev2<prev>d:n_wav=1
                            elif prev2>prev<d:n_wav=1
                        c,w=dp(idx+1,d,prev,ni_less,True)
                        tot_cnt+=c;tot_wav+=w+c*n_wav
                memo[state]=(tot_cnt,tot_wav)
                return memo[state]
            return dp(0,-1,-1,False,False)[1]
        return solve(str(num2))-solve(str(num1-1))