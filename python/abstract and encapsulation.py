class ATM:
    def __init__(self,balance):
        self.__balance=balance
    def credit(self,amount):
        self.__balance+=amount
        print(f"the credited amount is:{amount},the new balance is:{self.__balance}")
    def debit(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"the debited amount is:{amount},the new balance is:{self.__balance}")
        else:
            print("insufficent balance")
atm=ATM(0)
atm.credit(100)
atm.debit(5) 
#atm.balance=2000   #using private attribute we cannot access directly...






class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg_mark(self):
        sum=0
        for val in self.marks:
            sum+=val
        print(f"the student name is:{self.name} \navarage marks of student is:",sum/3)
s1=student("mateen",[10,20,30])
s1.avg_mark() 
s2=student("ironman",[40,50,60])
s2.avg_mark()