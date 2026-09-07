def amount_discount(price,qty):
    amount=price*qty
    if amount>=10000:
        discount = 0.1
    elif amount>= 5000:
        discount= 0.05
    else:
        discount= 0
    return amount-amount*discount

d = amount_discount(1000,10)
print(d)            


d = amount_discount(1000,5)
print(d)         


d = amount_discount(1000,1)
print(d)         