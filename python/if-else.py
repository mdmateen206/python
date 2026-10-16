#if elif else statement
age=int(input("enter the person age:"))
print("the person age is:",age)
if(age<=19):
    print("person cannot vote")
else:
    print("person can vote")

marks=int(input("enter the marks of the subject(1-100):"))
if(marks>=90):
    print("A grade")
elif(marks>=80 | marks<90):
    print("B grade")
elif(marks>=70 | marks<80):
    print("C grade")
else:
    print("fail")