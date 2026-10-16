#map....
num=[1,2,3,4,5]
def add(x):
    return x*2
res=map(add,num)
print(list(res))

num=[1,2,3,4,5,6]
res=map(lambda x:x*2,num)
print(list(res))

a=[1,2,3,4]
b=[5,6,7,8]
res=map(lambda x,y:x+y,a,b)
print(list(res))

#filter
num=[1,2,3,4,5]
def odd(x):
    return x%2!=0
res=filter(odd,num)
print(list(res))

res=filter(lambda x:x%2==0,num)
print(list(res))

#reduce.....
from functools import reduce
num=[1,2,3,4,5,6]
res=reduce(lambda x,y:x+y,num)
print(res)
num=[1,2,3,4,5]
def add(a,b):
    return a+b
res=reduce(add,num)
print(res)



from functools import reduce
score=[10,30,35,70,79,50,45,90,99,95,80]
#using map fun add 5 marks grace
grace=list(map(lambda x:x+5,score))
print("the grace marks are:",grace)
#using filter seeing pass or fail..
passes=list(filter(lambda x:x>50,grace))
print("the pass marks are:",passes)
#using reduce fun can cal total marks...
total=reduce(lambda x,y:x+y,passes)
print("the total score is:",total)