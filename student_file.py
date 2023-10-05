def menu():
    print("1:Append",end="\t\t\t")
    print("2:Delete",end="\t\t\t")
    print("3:Update")
    print("4:search stno",end = "\t\t\t")
    print("5:search name",end =  "\t\t\t")
    print("6:report all")
    print("7:Exit")
    choose = int(input(" " * 30+"Select 1 to 7:"))
    return choose

def findstno(stno):
    myfile = open("file.cvc","+a")
    myfile.seek(0)
    lines = myfile.readlines()
    recno = 0
    for line in lines:
        currecord = line.split(',')
        if(stno == currecord[0]):
            return recno
        recno = recno +1
    myfile.close()
    return -1

def findname(fname,lname):
    myfile = open("file.cvc","+a")
    myfile.seek(0)
    lines = myfile.readlines()
    recono = 0
    for line in lines:
        currecord = line.split(',')
        if(fname == currecord[1] and lname == currecord[2]):
            return recono
        recono = recono + 1
    myfile.close()
    return -1

def insert():
    stno = input("Enter stno:")
    recno = findstno(stno)
    if recno == -1:
        fname = input("\nEnter first name:")
        lname = input("\nEnter last name:")
        average = float(input("\nEnter average:"))
        line = stno+ ","+ fname+ ","+lname+ "," +str(average)+"\n"
        myfile = open("file.cvc","+a")
        myfile.write(line)
        myfile.close()
    else:
        myfile = open("file.cvc")
        lines = myfile.readlines()
        currecord = lines[recno].split(',')
        printinfo(currecord)
        myfile.close()
    return

def printinfo(currecord):
    print("-"*40)
    print("student number : ", currecord[0])
    print("First name : ", currecord[1])
    print("Last name : ",currecord[2])
    print("Average :",currecord[3])
    
    return

def delete():
    stno = input("Enter stno:")
    recno = findstno(stno)
    if recno != -1:
        myfile = open("file.cvc")
        lines = myfile.readlines()
        currecord = lines[recno].split(',')
        printinfo(currecord)
        ans = input("Are you sure that is delete?")
        if ans == 'y' or ans == 'Y':
            del lines[recno]
        myfile.close()
        myfile = open("file.cvc","w")
        myfile.writelines(lines)
        myfile.close()
    else:
        print(""*12,"student number",stno,"not found in file")
        
def update():
    stno = input("Enter stno:")
    recno = findstno(stno)
    if recno != -1:
        myfile = open("file.cvc")
        lines = myfile.readlines()
        currecord = lines[recno].split(',')
        printinfo(currecord)
        fname = input("Enter first name:")
        lname = input("Enter last name:")
        average = float(input("Enter average:"))
        line = stno +','+fname+','+lname+','+str(average)+'\n'    
        ans = input("Are you sure that is update?")
        if ans =='y' or ans == 'Y':
            lines[recno] = line
            myfile.close()
            myfile = open("file.cvc","w")
            myfile.writelines(lines)
            myfile.close()
        else:
            print(" "+12,"student number",stno,"not found in file")
            
def searchname():
    fname = input("Enter first name:")
    lname = input("Enter last  name: ")
    recno = findname(fname,lname)
    if recno != -1:
        myfile = open("file.cvc")
        lines = myfile.readlines()
        currecord = lines[recno].split(',')
        printinfo(currecord)
        myfile.close()
    else:
        print(""*10,"first name",fname,"last name",lname,"not found in file")
        
def searchstno():
    stno = input("Enter stno:")
    recno = findstno(stno)
    if recno !=-1:
        myfile =open("file.cvc")
        lines = myfile.readlines()
        currecord = lines[recno].split(',')
        printinfo(currecord)
        myfile.close()
    else:
        print(" "*12,"student number",stno,"not found in file")
        
def reportall():
    myfile =open("file.cvc","r")
    lines = myfile.readlines()  
    print("stno",end='\t\t')
    print("Fname", end='\t\t')
    print("Lname",end='\t\t')
    print("average ")
    print("="*70)
    sum = 0
    for line in lines:
        currecord = line.split(',')
        print(currecord[0],end='\t\t')
        print(currecord[1],end='\t\t') 
        print(currecord[2],end='\t\t')
        print(currecord[3])
        sum = sum + float(currecord[3])
        if len(lines) > 0:
            print(" " *30,"average total=",sum/len(lines))
        myfile.close()
    return

while True:
    choose = menu()
    if choose == 7:
        break
    if choose == 1:
        insert()
    if choose == 2:
        delete()
    if choose == 3:
        update()
    if choose == 4:
        searchstno()
    if choose == 5:
        searchname()
    if choose == 6:
        reportall()    
    print("*"*75)
    