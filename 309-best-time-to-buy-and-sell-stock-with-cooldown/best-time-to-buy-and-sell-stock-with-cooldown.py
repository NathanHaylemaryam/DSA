class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        hold, sold, rest = -prices[0], 0, 0
        for i in range(1, n):
            hold, sold, rest = max(hold, rest - prices[i]), hold + prices[i], max(rest, sold)
        return max(sold, rest)

        