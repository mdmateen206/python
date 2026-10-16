num=int(input("a:"))
try:
    print(10/num)
except ZeroDivisionError:
    print("zero is not divided")
except ValueError:
    print("enter the valid number:")
else:
    print("result:",10/num)
finally:
    print("wonder full!!!")


boy=input("who do you want to marry:")
try:
    if boy.lower()!="mateen":
        raise Exception("there is no another option!!,you want to marry Mateen")
except Exception as e:
    print(f"error:{e}")
else:
    print("mateen is ready!!")
finally:
    print("congrates")

file=input("enter the file name:")
try:
    if file.lower()!="python.py":
        raise Exception(f"there is no file name {file}")
except Exception as e:
    print(f"Error:{e}")
else:
    print(f"file {file} is opening")
finally:
    print("program end!!")


age=int(input("enter the age of person:"))
current_year=int(input("enter the current year:"))
try:
    if age==0 or current_year==0:
        raise Exception("invalid number!!")
except Exception as e:
    print(f"Error:{e}")
else:
    print("Age:",age)
    print("A person can turn into 100 yearold in:",current_year+(100-age))
finally:
    print("great!!!")