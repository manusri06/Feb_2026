class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        
        if k == n:
            return sum(cardPoints)

        ws = n-k
        tsum = sum(cardPoints)
        wsum = sum(cardPoints[:ws])
        mini = wsum
        for i in range(ws,n):
            wsum += cardPoints[i]-cardPoints[i-ws]
            mini = min(mini,wsum)
        return tsum - mini

"""  ms = 0
        n = len(cardPoints)

        for i in range(k+1):
            cs = 0
            for l in range(i):
                cs+=cardPoints[l]
            for r in range(k-i):
                cs += cardPoints[n-1-r]
            ms = max(ms,cs)
        return ms
 """