t = int(input())
for _ in range(t):
    n = int(input())
    stock = list(map(int, input().split()))
    profit = 0
    max_price = 0

    for price in reversed(stock):
        if price > max_price:
          max_price = price
        else:
          profit += max_price - price

    print(profit)