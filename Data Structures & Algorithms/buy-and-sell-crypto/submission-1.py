class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        for i in range(len(prices)) :
            for j in range(i+1, len(prices)) :
                profits.append(prices[j]- prices[i]) 
        if len(prices) > 1 and max(profits) > 0 :
            return max(profits)
        return 0