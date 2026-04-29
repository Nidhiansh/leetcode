class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res=[]
        def backtrack(i,cur):
            if i==len(digits):
                res.append(cur[:])
                return
            for c in d[digits[i]]:
                backtrack(i+1,cur+c)
        backtrack(0,"")
        return res