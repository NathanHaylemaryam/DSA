class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        stack = []

        n = len(prices)

        stack.append(prices[0])

        for price in prices:

            if stack and stack[-1] > price:

                stack.pop()

                stack.append(price)
            else:
                profit = max(profit , price - stack[-1])

        return profit

            