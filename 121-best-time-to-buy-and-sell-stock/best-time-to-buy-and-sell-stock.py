class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float("inf")
        maxProfit = 0 

        for price in prices:
            profit = price - minPrice
            if price < minPrice:
                minPrice = price
            maxProfit = max(profit,maxProfit)
        return maxProfit