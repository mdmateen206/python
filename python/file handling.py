#file=open(r"data3.txt","w")
#file.write("they are brothers......\n")
#file.close()


#with open(r"data1.txt","r") as file:
    #context=file.read()
    #print(context)



#students=["mateen", "saad", "ali", "ahmed", "bilal"]
#with open(r"data2.txt","w") as file:
   # for student in students:
       # file.write(f"{student}\n")


with open(r"data2.txt","r") as file:
    for line in file:
        print("students:", line.strip())