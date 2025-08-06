amount = int(input("how many items you want to purchase? "))
item_name = []
price = []
for i in range(amount):
    n = input(f"enter the name of the item:{i + 1} ")
    item_name.append(n)
    p = float(input(f"enter the price:{i + 1} "))
    price.append(p)
for i in range(amount):
    print(item_name[i], ":", price[i])
total = 0
for prices in price:
    total = prices + total

print(f"total:{total}")