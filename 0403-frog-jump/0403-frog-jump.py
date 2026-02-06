class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False

        dp = {stone:[] for stone in stones}
        dp[0].append(0)

        for stone in stones:
            for j in dp[stone]:
                for k in (j,j-1,j+1):
                    if k>0 and stone+k in dp:
                        if k not in dp[stone+k]:
                            dp[stone+k].append(k)

        return len(dp[stones[-1]]) > 0