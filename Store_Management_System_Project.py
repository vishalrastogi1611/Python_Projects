# major project by sql 
# Major Project on Store Management System

# import libraries
import mysql.connector 

# Create MySQL Object and Cursor
try:
    conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="7678",
    database="store"
        )
    cur = conn.cursor()
except Exception as e:
    print(e)

# A Method to Add a customer.
def addCus():
    name = input("\n\tEnter Customer Name : ")
    add = input("\tEnter Customer Address : ")
    mobile = input("\tEnter Mobile Number : ")
    query = "insert into customer(cname,cadd,mobile) value('"+name+"','"+add+"','"+mobile+"')"
    cur.execute(query)
    conn.commit()
    print("\n\tCustomer Added Successfully!")
    input("\n\t--- Press Enter To Continue...")


# A Method to view All Customers.
def viewAllCus():
    query = "select * from customer"
    cur.execute(query)
    data = cur.fetchall()
    print("\n\tAll Customers Are Here\n")
    for cus in data:
        print("\t",cus[0],'-',cus[1],'-',cus[2],'-',cus[3])
    input("\n\t--- Press Enter Key To Continue...")

# A Method to add a product in Database
def addPro():
    name = input("\n\tEnter Product Name : ")
    price = input("\tEnter Product Price : ")
    query = "insert into product(pname,price) value(%s,%s)"
    data = (name,price)
    cur.execute(query,data)
    conn.commit()
    print("\n\tProduct Added Successfully!")
    input("\n\t--- Press Enter To Continue...")

# A Method to view All Products.
def viewAllPro():
    query = "select * from product"
    cur.execute(query)
    data = cur.fetchall()
    print("\n\tAll Products Are Here\n")
    for cus in data:
        print("\t",cus[0],' - ',cus[1],' - ',cus[2])
    input("\n\t--- Press Enter Key To Continue...")    

# A Method to view A Product.
def viewPro():
    pid = input("\n\tEnter Product ID : ")
    query = "select * from product where pid="+pid
    cur.execute(query)
    cus = cur.fetchone()
    if(cus != None):
        print("\n\tProduct is Here\n")
        print("\tProduct ID : ",cus[0])
        print("\tProduct Name : ",cus[1])
        print("\tProduct Price : ",cus[2])
    else:
        print("\n\tProduct Not Found!")
    input("\n\t--- Press Enter Key To Continue...")

# A Method to delete a product.
def delPro():
    pid = input("\n\tEnter Product ID : ")
    query = "DELETE FROM product WHERE pid="+pid
    cur.execute(query)
    conn.commit()
    if(cur.rowcount != 0):
        print("\n\tProduct Deleted Successfully!")
    else:
        print("\n\tProduct Not Found!")
    input("\n\t--- Press Enter To Continue...")

# A Method to check Product Availablity
def checkPro(pid):
    query = "select * from product where pid="+pid
    cur.execute(query)
    cur.fetchall()
    if(cur.rowcount == 0):
        return False
    else:
        return True
# A Method to check Customer Availablity
def checkCus(cid):
    query = "select * from customer where cid="+cid
    cur.execute(query)
    cur.fetchall()
    if(cur.rowcount == 0):
        return False
    else:
        return True

# A Method to Place an Order
def placeOrder():
    cid = input("\n\tEnter Customer ID : ")
    pid = input("\tEnter Product ID : ")
    qty = input("\tEnter Quantity : ")
    if( checkPro(pid) and checkCus(cid) ):
        query = "INSERT INTO orders(cid,pid,qty) VALUE(%s,%s,%s)"
        data = (cid,pid,qty)
        cur.execute(query,data)
        conn.commit()
        print("\n\tOrder Placed Successfully!")
    else:
        print("\n\tEither PID or CID is incorrect!")
    input("\n\t--- Press Enter To Continue...")

# A Method to view all orders
def viewAllOrders():
    query = '''
SELECT cname,pname,price,qty,price*qty FROM customer
JOIN orders
ON customer.cid = orders.cid
JOIN product
ON orders.pid = product.pid'''
    cur.execute(query)
    data = cur.fetchall()
    print("\n\tName - Product - Price - Qty - Net_Amount\n")
    for o in data:
        print("\t",o[0]," - ",o[1]," - ",o[2]," - ",o[3]," - ",o[4])
    input("\n\n\t--- Press Enter To Continue...")

# A Method to view an order by customer ID
def viewOrder():
    cid = input("\n\tEnter Customer ID : ")
    query = '''SELECT cname,pname,price,qty,price*qty FROM customer
JOIN orders
ON customer.cid = orders.cid
JOIN product
ON orders.pid = product.pid
WHERE customer.cid = '''+cid
    cur.execute(query)
    d = cur.fetchall()
    if(cur.rowcount != 0 ):
        for data in d:
            print("\n\tCustomer Name : ",data[0])
            print("\tProduct Name : ",data[1])
            print("\tProduct Price : ",data[2])
            print("\tProduct Quantity : ",data[3])
            print("\tNet Amount : ",data[4])
    else:
        print("\n\tNo Order Found on This Customer ID")
    input("\n\t--- Press Enter To Continue...")


# DASHBOARD
while True:
    print("\n\t***** STORE MANAGEMENT SYSTEM *****\n")
    print("\t1. Add Customer")
    print("\t2. View All Customer")
    print("\t3. Add Product")
    print("\t4. View All Products")
    print("\t5. View A Product By ID")
    print("\t6. Delete A Product")
    print("\t7. Place an Order")
    print("\t8. View All Orders")
    print("\t9. View An Order")
    print("\t0. Exit")
    ch = int(input("\n\tEnter Your Choice : "))
    if(ch==0):
        print("\n\t--- Bye-Bye Admin!")
        break
    elif(ch==1):
        addCus()
    elif(ch==2):
        viewAllCus()
    elif(ch==3):
        addPro()
    elif(ch==4):
        viewAllPro()
    elif(ch==5):
        viewPro()
    elif(ch==6):
        delPro()
    elif(ch==7):
        placeOrder()
    elif(ch==8):
        viewAllOrders()
    elif(ch==9):
        viewOrder()

