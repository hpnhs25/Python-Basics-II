## zero_coupon_bonds example

import fvmodule

price = 400

future_value = 1000
discount_rate = 0.1
comp_period = 1
years = 5

bond_value = fvmodule.calculate_pv(future_value, discount_rate, comp_period, years)

if bond_value > price:
    discount = round(bond_value - price, 2)
    print(f"The bond is selling at a price of {price}, and is valued at ${bond_value}")
    print(f"A discount of ${discount} exists, therefore you want to BUY the bond")
elif bond_value < price:
    premium = round(price - bond_value, 2)
    print(f"The bond is selling at a price of {price}, and is valued at ${bond_value}")
    print(f"A premium of ${premium} exists, therefore you do NOT want to buy the bond")
else:
    print(f"The bond is selling at a price of {price}, and is valued at ${bond_value}")
    print(f"The bond is selling at its present value, you are neutral")