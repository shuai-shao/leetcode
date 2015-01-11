class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        return sum([prices[i+1]-prices[i] for i in range(len(prices)-1) if prices[i+1]>prices[i]])
        
