# actually same problem as find maximum addition subarray
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        all_profit = 0
        pre_profit = 0
        for i in range(1,len(prices)):
            delta = prices[i] - prices[i-1]
            cur_profit = max(delta, pre_profit + delta)
            all_profit = max(all_profit, cur_profit)
            pre_profit = cur_profit
        return all_profit
