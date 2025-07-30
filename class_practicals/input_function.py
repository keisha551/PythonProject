'''

ask user to enter the grade
calculating average grades
display the total grade
'''


grade1=int(input("enter grade :"))
grade2=int(input("enter grade :"))
grade3=int(input("enter grade :"))
grade4=int(input("enter grade :"))
#calculate average
total_grades=grade1+grade2+grade3+grade4
print(total_grades)
average=total_grades/4
print(average)
print("average:",average)
if(total_grades>=80):
    print("A")
elif(total_grades>=60):
    print("B")
elif(total_grades>=50):
    print("C")
else:
    print("fail")


