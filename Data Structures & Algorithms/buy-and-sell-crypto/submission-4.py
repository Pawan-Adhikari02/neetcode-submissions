class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range (len(prices)-i):
                if ((prices[j+i]-prices[i])>profit):
                    profit = (prices[i+j]-prices[i])
        return profit