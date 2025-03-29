#  import module
import pickle
import os

# FUNCTION TO ADD A STUDENT
def addStu():
    file = open("student.dat","ab")
    rollno = input("\n\tEnter Student Roll No : ")
    name = input("\tEnter Student Name : ")
    course = input("\tEnter Student Course Name : ")
    fee = input("\tEnter Course Fee : ")
    addr = input("\tEnter Course address : ")
    phone = input("\tEnter Course phone : ")    
    pickle.dump(rollno,file)
    pickle.dump(name,file)
    pickle.dump(course,file)
    pickle.dump(fee,file)
    pickle.dump(addr,file)
    pickle.dump(phone,file)
    print("\n\t--- Student Added Successfully!")
    input("\n\tPress Enter To Continue...")
    file.close()

# FUNCTION TO VIEW ALL STUDENTS
def viewAllStu():
    try:
        file = open("student.dat","rb")
        count = 0
        print("\nRoll\tName\tCourse\tFee\taddr\tphone\n")
        while True:
            count=count+1
            data = pickle.load(file)
            print(data,end="\t")
            if(count%6==0):
                print()
        file.close()
    except:
        print("\n\tAll Students Are Loaded!")
    input("\n\t--- Press Enter To Continue...")
    file.close()

# FUNCTION TO VIEW A STUDENT BY ROLL NO
def viewStu():
    stuFound = 0
    try:
        file = open("student.dat","rb")
        roll = input("\n\tEnter Student Roll No : ")
        while True:
            data = pickle.load(file)
            if(data==roll):
                print("\n\tRoll No : ",data)
                print("\tName : ",pickle.load(file))
                print("\tCourse : ",pickle.load(file))
                print("\tFee : ",pickle.load(file))
                print("\taddr : ",pickle.load(file))
                print("\tphone : ",pickle.load(file))
                stuFound = 1
        file.close()
    except:
        if(stuFound==0):
            print("\n\tStudent Not Found!")
        else:
            print("\n\tHere is Your Student!")
        input("\n\t--- Press Enter To Continue...")
        file.close()

# FUNCTION TO DELETE A STUDENT
def deleteStu():
    stuFound = 0
    try:
        file1 = open("student.dat","rb")
        file2 = open("temp.dat","ab")
        roll = input("\n\tEnter Student Roll No : ")
        while True:
            data = pickle.load(file1)
            if(data==roll):
                pickle.load(file1)
                pickle.load(file1)
                pickle.load(file1)
                pickle.load(file1)
                pickle.load(file1)
                stuFound = 1
            else:
                pickle.dump(data,file2)
        file1.close()
        file2.close()
    except:
        if(stuFound==0):
            print("\n\tStudent Not Found!")
        else:
            print("\n\tStudent Deleted Successfully!")
        input("\n\t---Press Enter To Continue...")
        file1.close()
        file2.close()
        os.remove("student.dat")
        os.rename("temp.dat","student.dat")
        
# FUNCTION TO UPDATE INFO OF A STUDENT
def updateStu():
    file1 = open("student.dat","rb")
    file2 = open("temp.dat","ab")
    roll = input("\n\tEnter Roll No To Update : ")
    stuFound = 0
    try:
        while True:
            data = pickle.load(file1)
            if(data==roll):
                name = pickle.load(file1)
                print("\n\tRoll No : ",data)
                print("\tName : ",name)
                pickle.dump(data,file2)
                pickle.dump(name,file2)
                course = input("\tEnter Course Name : ")
                fee = input("\tEnter Course Fee : ")
                addr = input("\tEnter Course addr : ")
                phone = input("\tEnter Course phone : ")
                pickle.dump(course,file2)
                pickle.dump(fee,file2)
                pickle.dump(addr,file2)
                pickle.dump(phone,file2)
                pickle.load(file1)
                pickle.load(file1)
                pickle.load(file1)
                pickle.load(file1)
                stuFound = 1
            else:
                pickle.dump(data,file2)
    except:
        if(stuFound==1):
            print("\n\tStudent Updated Successfully!")
        else:
            print("\n\tStudent Not Found!")
        input("\n\tPress Enter To Continue...")
    file1.close()
    file2.close()
    os.remove("student.dat")
    os.rename("temp.dat","student.dat")
    

# FUNCTION TO COUNT TOTAL STUDENTS
def totalStu():
    file = open("student.dat","rb")
    count = 0
    try:
        while True:
            pickle.load(file)
            count=count+1
    except:
        print("\n\tTotal Students : ",count//6)
        input("\n\tPress Enter To Continue...")

# DASHBOARD
while(True):
    print("\n\n\t***** INSTITUTE MANAGEMENT SYSTEM **** *")
    print("\n\t1. Add Student")
    print("\t2. View All Students")
    print("\t3. View A Student By Roll No")
    print("\t4. Delete A Student")
    print("\t5. Update A Student")
    print("\t6. Check Total Students")
    print("\t7. Exit")
    ch = int(input("\n\tEnter Your Choice : "))
    if(ch==7):
        print("\n\t--- Bye-Bye Admin!")
        break
    elif(ch==1):
        addStu()
    elif(ch==2):
        viewAllStu()
    elif(ch==3):
        viewStu()
    elif(ch==4):
        deleteStu()
    elif(ch==5):
        updateStu()
    elif(ch==6):
        totalStu()
    else:
        input("\n\tWrong Entered\n\tTry Again!")
