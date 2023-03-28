def calculate_fv(present_value, interest_rate, comp_period, years):
    ### FV = PV * (1 + i/n) ** (n*t)
    fv = present_value * ((1 + (interest_rate / comp_period)) ** (comp_period * years))
    fv_formatted = round(fv, 2)
    return fv_formatted

def calculate_pv(future_value, discount_rate, comp_period, years):
    ### PV = FV / (1 + i/n) ** (n*t)
    pv = future_value / ((1 + (discount_rate / comp_period)) ** (comp_period * years))
    pv_formatted = round(pv, 2)
    return pv_formatted

