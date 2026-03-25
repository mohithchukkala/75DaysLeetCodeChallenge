class Solution(object):
    def maxProfit(self, prices):
        buy=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if buy>prices[i]:
                buy=prices[i]
            if prices[i]-buy>profit:
                profit=prices[i]-buy
        return profit