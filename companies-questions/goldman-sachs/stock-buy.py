def max_profit(list, days):
    profit = 0
    for i in range(1, days):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit


prices = [100, 180, 260, 310, 40, 535, 695]
profit = max_profit(prices, len(prices))
print(profit)
