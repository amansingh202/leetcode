stock_prices = [298,305,320,301,292]

result = stock_prices[3]

print(result)

#searching by value
for i in range(len(stock_prices)):
    if stock_prices[i] == 301:
        print(i)