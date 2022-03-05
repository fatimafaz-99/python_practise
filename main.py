# Strings formats in python

price_string="the price of {} is {}"
apple_price =price_string.format("apple", "50")

print(apple_price)   # the price of apple is 50


# taking user input and string manipulation
originalprice = input("enter the original price of product ")
discountedprice = int(originalprice)-(int(originalprice)*50)/100
print(
    f"this discounted price of {originalprice} after 50% discount is {discountedprice}")
#enter the original price of product 100
#this discounted price of 100 after 50% discount is 50.0
