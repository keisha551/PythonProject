num=int(input("how many items to purchase?"))
item_price={}
for i in range(num):
    item=input("name of item: ")
    price=int(input("enter the price: "))
    item_price[item]=price
print(item_price)
print(sum(item_price.values()))
total=0
for i,j in item_price.items():
    total=j+total
print(f"total:{total}")