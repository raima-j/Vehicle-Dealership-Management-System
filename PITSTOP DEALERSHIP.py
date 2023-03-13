import mysql.connector
import datetime
import time

mydb=mysql.connector.connect(host="localhost",user="root" , passwd="password", database="pitstop")
mycursor=mydb.cursor()
print ('\n\n-----------------------------✨ ✨ ✨ WELCOME!✨ ✨ ✨------------------------------')
time.sleep(0.5)

def displayCar():
    sql="select * from car"
    mycursor.execute(sql)
    res=mycursor.fetchall()
    print('\nCar records are:\n')
    time.sleep(0.5)
    print("model_no  |   model_name  |   mnf_name     |  branch_id")
    print("----------|---------------|----------------|-----------")
    #print("")
    for i in res:
        print('%0-10s %0-20s %0-20s %0-10s' % i)

def displayStock():
    sql="select * from stock"
    mycursor.execute(sql)
    res=mycursor.fetchall()
    print('\nCar records are:\n')
    time.sleep(0.5)
    print("model_no  |   model_name  |   mnf_name     |  branch_id")
    print("----------|---------------|----------------|-----------")
    #print("")
    for i in res:
        print('%0-10s %0-20s %0-20s %0-10s' % i)

def insertCar():
    L=[]
    stk=[]
    
    print(" \t---> Inserting into Branch Details.\n")
    time.sleep(1.5)
    m_no=input("Enter the Model Number:")
    L.append(m_no)
    iname=input("Enter the Model Name:")
    L.append(iname)
    mnf=input("Enter the Manufacturer Name: ")
    L.append(mnf)
    branch_id=input("Enter the Branch ID:")
    L.append(branch_id)
    car=L
    sql="insert into car(model_no,model_name,mnf_name,branch_id) values(%s,%s,%s,%s)"
    mycursor.execute(sql,car)
    mydb.commit()
    res=mycursor.fetchall()
    sql="insert into stock(model_no,model_name,mnf_name,branch_id) values(%s,%s,%s,%s)"
    mycursor.execute(sql,car)
    mydb.commit()
    res=mycursor.fetchall()
    time.sleep(1)
    print("\nModel has been added.")
    time.sleep(1)
    displayStock()
    MenuSet()

def editcar():
    print(" \t---> Editing Branch Details.\n")
    time.sleep(1)
   
    displayStock()
    
    time.sleep(1)
    m_no=input("\nEnter model number to be edited:")
    sql="select * from car where model_no= %s"
    ed=[m_no]
    mycursor.execute(sql,ed)
    res=mycursor.fetchall()
    time.sleep(1)
    print("model_no  |   model_name  |   mnf_name     |  branch_id")
    print("----------|---------------|----------------|-----------")
    for i in res:
        print('%0-10s %0-20s %0-20s %0-10s' % i)
    print("")

    fid=input("\nEnter the field name you want to edit:")
    v=input("Enter the value you want to set:")
    sql="Update car set %s='%s' where model_no='%s'" % (fid,v,m_no)
    
    mycursor.execute(sql)
    sql="Update stock set %s='%s' where model_no='%s'" % (fid,v,m_no)
    
    mycursor.execute(sql)
    time.sleep(1)
    print("\nRecords after editing:")
    time.sleep(0.5)
    displayCar()
    print("\n")
    mydb.commit()
    MenuSet()

def delcar():
    print(" \t---> Deleting from Branch Details.\n")
    time.sleep(1)
    
    displayStock()

    m_no=input("\nEnter the Model No to be deleted:")
    sql="delete from stock where model_no =%s"
    cid=[m_no]
    mycursor.execute(sql,cid)
    mydb.commit()

    time.sleep(1)
    print("\nONE CAR HAS BEEN DELETED.\n")
    time.sleep(1)

    sql="select * from car_archive"
    mycursor.execute(sql)
    res=mycursor.fetchall()
    print('\nArchived records are:\n')
    time.sleep(0.5)
    print("model_no  |   model_name  |   mnf_name     |  branch_id")
    print("----------|---------------|----------------|-----------")
    for i in res:
        print('%0-10s %0-20s %0-20s %0-10s' % i)
   
    MenuSet()

def viewcar():
    print("\n\t---> Viewing Branch Details.\n")
    time.sleep(1.5)
    print("\nPlease select the category to display data:\n")
    print("1 For basic details of the branch.")
    print("2 For All Car details with their service centers.")
    print("3 For details of a specific manufacturer.")
    print("4 For number of bought cars for each manufacturer.")
    print("5 For Owner details.")
    print("6 For Sale details.\n")
    print("7 For archived car details.\n")
    print("Any other key for returning to main menu.\n)")

    ch=int(input("\nEnter your choice to Display:"))

    x=0
    if (ch==1):
        sql="select c.model_no, c.model_name, b.branch_id,b.city, m.mnf_id,m.mnf_name from car c, dealership_branch b, manufacturer m where c.branch_id=b.branch_id and c.mnf_name=m.mnf_name"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        time.sleep(0.5)
        print('\nRecords are:\n')
        time.sleep(0.5)
        print("model_no |   model_name  | branch_id |    city     |   mnf_id  |   mnf_name   |")
        print("---------|---------------|-----------|-------------|-----------|--------------|")
        for i in res:
            print("%0-10s %0-20s %0-10s %0-20s %0-10s %0-20s" % i)
        x=1

    elif (ch==2):
        sql="select c.model_no, c.model_name, s.center_id from car c, dealership_branch b, service_centers s where c.branch_id=b.branch_id and s.branch_id=b.branch_id"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        time.sleep(0.5)
        print('\nRecords are:\n')
        time.sleep(0.5)
        print("model_no  |   model_name  |   center_id     |")
        print("----------|---------------|-----------------|")
        for i in res:
            print("%0-10s %0-20s %0-10s " % i)
        x=1
        
    elif(ch==3):
        m='mnf_name'
        v=input("Enter the name of the manufacturer:")
        sql="select * from manufacturer where "+m+" = %s "
        #sq=sql
        tp=[v]
        mycursor.execute(sql,tp)
        res=mycursor.fetchall()
        time.sleep(0.5)
        print('\nRecords are:\n')
        time.sleep(0.5)
        print("  mnf_id  |   mnf_name  |   mnf_country   |")
        print("----------|-------------|-----------------|")
        for i in res :
                print("%0-10s %0-20s %0-20s" %i)
        x=1

    elif(ch==4):
        sql="select mnf_id as 'Manufacturer',count(*) from owners group by mnf_id"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        time.sleep(0.5)
        print('\nRecords are:\n')
        time.sleep(0.5)
        print("  Manufacturer | count(*)    |")
        print("---------------|-------------|")
        for i in res:
            print("%0-15s %0-10s" % i)
        x=1

    elif(ch==5):
        sql="select * from owners"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        time.sleep(0.5)
        print('\nRecords are:\n')
        time.sleep(0.5)
        print("  owner_id  |   model_no  |   model_name   | mnf_id  | branch_id |")
        print("------------|-------------|----------------|---------|-----------|")
        for i in res:
            print("%0-10s %0-10s %0-20s %0-10s %0-10s" % i)
        x=1

    elif(ch==6):
        sql="select purchase.owner_id, car.model_no , car.model_name,purchase.mnf_id, car.mnf_name, car.branch_id , purchase.cost from car cross join purchase on car.model_no=purchase.model_no order by purchase.owner_id;"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        time.sleep(0.5)
        print('\nRecords are:\n')
        time.sleep(0.5)
        print(" owner_id |  model_no |   model_name  | mnf_id  |  mnf_name   | branch_id |  cost  |")
        print("----------|-----------|---------------|---------|-------------|-----------|--------|")
        for i in res:
            print("%0-10s %0-10s %0-20s %0-10s %0-10s %0-10s %0-10s" % i)
        x=1

    elif(ch==7):
        sql="select * from car_archive"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        print('\nArchived records are:\n')
        time.sleep(0.5)
        print("model_no  |   model_name  |   mnf_name     |  branch_id")
        print("----------|---------------|----------------|-----------")
        #print("")
        for i in res:
            print('%0-10s %0-20s %0-20s %0-10s' % i)
        x=1

    else:
        time.sleep(1)
        MenuSet()

    print(" ")
    time.sleep(1)
    MenuSet()

def purchasecar():
    
    time.sleep(1)

    displayStock()
    time.sleep(1)
    itemid=input("Enter model number: ")
   
    sql="select cost from purchase where model_no=%s"
    m_no=[itemid]
    mycursor.execute(sql,m_no)
    time.sleep(0.5)
    res=mycursor.fetchone()
    for i in res:
       print("The cost of your choice of model is:",i,'\n')
    
    print("Order for ",itemid," has been placed.\nFormalities shall be done in person.\nThank you.\n")
    time.sleep(1)
    sql="select * from car where model_no = %s "
    sq=sql
    tp=[itemid]
    mycursor.execute(sq,tp)
    model_no=mycursor.fetchall()
    time.sleep(0.5)
    print('\nPurchase Records are:\n')
    for i in model_no :
            print(i)
            
    x=1

    
    sql="set @list_id=''"
    sq=sql
    mycursor.execute(sq)
    sql="call num_id(@list_id)"
    sq=sql
    mycursor.execute(sq)
    sql="select @list_id"
    sq=sql
    mycursor.execute(sq)
    count_id=mycursor.fetchall()
    time.sleep(0.5)

    sql="insert into pricelist(select c.model_no,p.mnf_id,p.cost, (@list_id+1),c.branch_id from purchase p , car c where c.model_no=p.model_no and c.model_no=%s)"
    sq=sql
    tp=[itemid]
    mycursor.execute(sq,tp)
    print("\n")
    time.sleep(0.5)

    sql="insert into owners(select (@list_id+1),c.model_no,c.model_name,p.mnf_id,c.branch_id from purchase p , car c where c.model_no=p.model_no and c.model_no=%s)"
    sq=sql
    tp=[itemid]
    mycursor.execute(sq,tp)
    print("\nOne car has been purchased successfully!\n")
    
    MenuSet()


def MenuSet(): #Function For The Branch System
    time.sleep(1)
    print ("\n\n                        --- 🎶 --- PIT STOP LOBBY --- 🎶  ---                      ")
    time.sleep(1)
    print("\t\n---> Choose an option from the following:\n")
    print("Enter 1 : To Add car. ")
    print("Enter 2 : To Edit car ")
    print("Enter 3 : To Delete car ")
    print("Enter 4 : To View Various Branch details.")
    print("Enter 5 : To Purchase car.\n")
    
    
    try: #Using Exceptions For Validation
            userInput = int(input("Please Select An Above Option: ")) #Will Take Input From User
    except ValueError:
            print("\nNot a valid option. Terminating now!") #Error Message
            time.sleep(1)
            exit()
    else:
            print("\n") #Print New LineR
    if(userInput==1):
            insertCar()
    elif(userInput==2):
            editcar()
    elif (userInput==3):
            delcar()
    elif (userInput==4):
            viewcar()
    elif (userInput==5):
            purchasecar()
    else:
        time.sleep(1)
        print("\nPlease enter a valid option.\n")
    MenuSet()
MenuSet()