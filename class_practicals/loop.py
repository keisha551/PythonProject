grade=int(input("enter grade:"))
while grade>=100 or grade < 0:
    print("invalid score, pls enter a valid value")
    grade1=int(input("enter grade :"))
if (grade>=80):
    print("A")
    grade2=int(input("enter grade :"))
elif (grade>=60):
    print("B")
    grade3=int(input("enter third grade :"))
elif (grade>=50):
    print("C")
else:
    print("FAIL")


