class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
    
        l = 0
        res = 0
        for i in range(1,len(prices)):
            if (prices[i]-prices[l]) > res:
                res = prices[i]-prices[l]
            if prices[i] < prices[l]:
                l = i
        return res



        
        