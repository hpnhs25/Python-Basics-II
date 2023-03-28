def print_hello():
    print("Hello!")

def print_goodbye():
    print("Goodbye!")

#import numpy
import numpy_financial as npf

interest_rate = 0.1
cash_flow = [-1000, 400, 400, 400, 400]

net_present_value = npf.npv(interest_rate, cash_flow)
print(f"NPV of the project = ${net_present_value}")


