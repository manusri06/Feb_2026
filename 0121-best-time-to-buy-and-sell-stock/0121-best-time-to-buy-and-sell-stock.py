class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        maxi = 0
        for i in range(1,len(prices)):
            c = prices[i]-mini
            maxi = max(maxi,c)
            mini = min(mini,prices[i])

        return maxi
