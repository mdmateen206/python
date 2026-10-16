student={
    "name":"mateen",
    "age":19,
    "sgpa":7.5,
    "college":"HKBK college of engi",
    "city":"bengalure",
}
print(student)
student["city"]="nagavara"
student["age"]=20
print(student)
student.keys()
student.values()
for keys,values in student.items():
    print(f"{keys}:{values}")
student.get("college")
student.update({"state":"karnataka"})
print(student)
for keys,values in student.items():
    print(f"{keys}:{values}")


n=int(input("enter the number of students"))
names=[]
marks=[]
for i in range(n):
    name=input("enter the name of person:")
    mark=int(input("enter the marks of person:"))
    names.append(name)
    marks.append(mark)
print(names)
print(marks)
students={}
for i in range(len(names)):
    students[names[i]]=marks[i]
print(students)

with open(r"marks3.txt","w") as file:
    for name,mark in students.items():
        file.write(f"{name}-{mark} \n")