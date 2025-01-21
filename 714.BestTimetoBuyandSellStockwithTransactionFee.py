class Solution:
    def maxProfit(self, prices, fee):

        profit = 0
        buy_price = prices[0]

        for price in prices[1:]:
            if price < buy_price:
                buy_price = price
            elif price > buy_price + fee:
                profit += price - buy_price - fee
                buy_price = price - fee

        return profit
