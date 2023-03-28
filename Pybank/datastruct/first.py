
import fvmodule

present_value = 10000
interest_rate = 0.1
comp_period = 1
years = 3

future_value = fvmodule.calculate_fv(present_value,interest_rate,comp_period,years)

print(f"The future value of {present_value} is {future_value}")

