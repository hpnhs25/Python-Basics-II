
import testfunction
testfunction.print_hello()

from testfunction import print_hello
print_hello()

import testfunction as fun
fun.print_goodbye()

#import numpy 
import numpy_financial as npf

interest_rate = 0.1
cash_flow = [-1000, 400, 400, 400, 400]

net_present_value = npf.npv(interest_rate, cash_flow)
print(f"Net Present Value of the Project is ${net_present_value}")


