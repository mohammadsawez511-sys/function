def craete_dictionary(pname,price):
    #print(pname,price)
    my_product=dict()
    if len(pname)!=len(price):
        print(" pname and price do not match ")
    else:
        for i in range (len(pname)):
            my_product[pname[i]]=price[i]
    return my_product            


s = craete_dictionary(["keyboard","mouse","monitor"],[599,99,10000])
print(s)


# # simple way 
# print({'keyboard': 599, 'mouse': 99,})