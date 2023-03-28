#stock_dict={ 
#    "APPL": {
#        "name":"Apple",
#        "exchange":"NASDAQ",
#        "market_cap":900
#    },
#    "MU": {
#        "name":"Micron Technology",
#        "exchange":"NASDAQ",
#        "market_cap":40
#    },
#    "TSLA":{
#        "name":"Tesla",
#        "exchange":"NASDAQ",
#        "market_cap":1000
#    }

#}

#print(stock_dict)

#tsla_entry = stock_dict["TSLA"]
#tsla_name = stock_dict["TSLA"]["name"]
#tsla_name = tsla_entry["name"]
#tsla_exchange=stock_dict["TSLA"]["exchange"]
#tsla_cap=stock_dict["TSLA"]["market_cap"]

#print(tsla_entry)
#print(tsla_name)
#print(tsla_exchange)
#print(tsla_cap)

#type(stock_dict)
#type(tsla_entry)
#type(tsla_name)
#type(tsla_exchange)
#type(tsla_cap)


ceo_list = [
    ["Warren Buffet", 90, "CEO of Berkshire Hathaway"],
    ["Jeff Bezos", 58, "Former CEO of Amazon"],
    ["Harry Porter", 90, "Professor of Finance"]
]

first_entry = ceo_list[0]
firs_entry_name = ceo_list[0][0]
print(first_entry)
print(firs_entry_name)

ceo_list2 = [
    ["Warren Buffet", 90, "CEO of Berkshire Hathaway"],
    ["Jeff Bezos", 58, "Former CEO of Amazon"],
    {"name":"Harry Porter", "age":90, "title":"Professor of Finance"}
]

print(ceo_list2)
