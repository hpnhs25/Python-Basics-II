def calculate_market_cap (price, shares):
    cap = price * shares
    return cap

stock_price = 90.1
number_shares = 300

market_cap = calculate_market_cap(stock_price,number_shares)

print(f"Market Cap: {market_cap}")

add_ten = lambda x , y: x+y
a = add_ten(17,13)
print(a)

