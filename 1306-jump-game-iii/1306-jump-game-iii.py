class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        q=[start]
        while q:
            curr=q.pop(0)
            if arr[curr]==0:
                return True
            if arr[curr]<0:
                continue
            for nxt in (curr+arr[curr],curr-arr[curr]):
                if 0<=nxt<len(arr) and arr[nxt]>=0:
                    q.append(nxt)
            arr[curr]=-arr[curr]
        return False