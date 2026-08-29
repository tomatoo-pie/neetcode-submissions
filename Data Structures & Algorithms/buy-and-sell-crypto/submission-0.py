class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        mini = prices[0]
        maxprofit = 0
        while i < len(prices):
            if mini > prices[i]:
                mini = prices[i]
            maxprofit = max(maxprofit,prices[i]-mini)
            i+=1
        
        return maxprofit