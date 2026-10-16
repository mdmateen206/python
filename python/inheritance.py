#single inheritance
class parents:
    def __init__(self,surname):
        self.surname=surname
class child(parents):
    def __init__(self,surname,name):
        super().__init__(surname)
        self.name=name
        print(f"{self.surname} {self.name}")

p1=child("mohammed","mateen")

#multilevel inheritance
class parents:
    def __init__(self,surname):
        self.surname=surname
class child(parents):
    def __init__(self,surname,cname):
        super().__init__(surname)
        self.cname=cname
class gchild(child):
    def __init__(self,surname,cname,name):
        super().__init__(surname,cname)
        self.name=name
        print(f"{self.surname} {self.cname} {self.name}")
p1=gchild("mohammed","saad","mateen")

#multiple inheritance
class father:
    def __init__(self,fname):
        self.fname=fname
class mother:
    def __init__(self,mname):
        self.mname=mname
class child(father,mother):
    def __init__(self,fname,mname,name):
        father.__init__(self,fname)
        mother.__init__(self,mname)
        self.name=name
        print(f"{self.fname} {self.mname} {self.name}")
p1=child("nayeem","nazeema","mateen")

#heirarkid inhertance
class notification:
    def __init__(self):
        print("send")
class sms(notification):
    def __init__(self):
        print("sms send")
class email(notification):
    def __init__(self):
        print("email send")
n=notification()
e=email()
s=sms()