#assign grade
def total(average):
    avg=average
    if avg >=80:
        return "A"
    elif avg>=60:
        return"B"
    elif avg>=50:
        return "C"
    else:
        return "fail"