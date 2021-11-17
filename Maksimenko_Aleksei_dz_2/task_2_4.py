prices = [27.8, 35, 46.7, 44.07, 15, 0.9, 89.67, 103.2, 88,
          18.6, 56, 67.43, 34, 90.7, 100.09, 15.47, 78, 0.5]
print(prices)
print(f'id of a list is {id(prices)}')
prices.sort()
print(prices)
print(f'id is the same: {id(prices)}')
edited_prices = sorted(prices, reverse=True)
print(edited_prices)
top = edited_prices[0:5]
top.reverse()
print("Top prices:", top)
for el in range(len(prices)):
    edit_el = f'{prices[el]:.2f}'
    two_el = str(edit_el).split('.')
    rub = two_el[0]
    coin = two_el[1]
    prices[el] = f'{rub} руб {coin} коп'
print(*prices, sep=', ')
