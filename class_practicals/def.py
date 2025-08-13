  def capture_input():
    n=int(input("Enter how many marks"))
    marks=[]
    for i in range (n):
        mark=int(input("Enter how many marks: "))
        marks.append(mark)
    return marks
def average():
    scores=capture_input()
    avg=sum(scores)/len(scores)
    return avg
def grade():
    avg=averge()
    if avg >50:
        return "pass"
    else:
        return "fail"