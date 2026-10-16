#function is a block of code that perform specific task
def fun_name(parameter):
    pass
    return fun_name
def sum(a,b):
    add=a+b
    sub=a-b
    mult=a*b
    print(add)
    print(sub)
    print(mult)
    
    return 
sum(4,2)
sum(3,3)
sum(10,2)

def avg_num(a,b,c=0):
    avg=(a+b+c)/3
    print(avg)
    return
avg_num(10,20)
avg_num(20,30,50)

def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
    return
cal_fact(5)
cal_fact(3)










#recursion: when fun call itself repeatedly.........
def show(n):
    if(n==0):
        return 0
    print(n)
    show(n-1)
show(4)

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return fact(n-1)*n
    return
fact(5)