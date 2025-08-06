score=[20,10,5,10,20]
score.remove(5)
score.append(30)
print(score)

total=0
for i in score:
    total+=i
print(total)
numbers=[40,-20,60,4,-4,-8]
positive_numbers=[num for num in numbers if num > 0]
negative_numbers=[num for num in numbers if num < 0]
numbers=i.split