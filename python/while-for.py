#while loop
i=1
while(i<=5):
    print("hello world")
    i+=1
i=1
while(i<=4):
    print(i)
    i+=1

i=1
while(i<=10):
    print(90*i)
    i+=1

i=1
while(i<=10):
    print(i)
    i+=1

i=10
while(i>=1):
    print(i)
    i-=1

i=1
while(i<=5):
    print(i)
    if(i==4):
        break
    i+=1




#for loop
num=[1,2,3,4,5]
for i in num:
    print(i)

for i in range(0,10,2):
    print(i,end=" ")
print("\t")
for i in range(0,100,5):
    print(i,end=" ")

for i in range (100,1,-5):
    print(i)