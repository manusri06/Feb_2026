class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        if len(answerKey) == k:
            return k
        l = ans = 0
        mf = 0
        dict = {}
        for r in range(len(answerKey)):
            if answerKey[r] not in dict:
                dict[answerKey[r]] = 0
            dict[answerKey[r]]+=1
            mf = max(mf,dict[answerKey[r]])

            while (r-l+1)-mf > k:
                dict[answerKey[l]]-=1
                l+=1
           
            ans = max(ans,r-l+1)
        return ans