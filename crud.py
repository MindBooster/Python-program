import mysql.connector as ms
from tabulate import tabulate
x=ms.connect(host="localhost", user="root", database="emp",passwd="123")
if x.is_connected():
    ans='y'
    while ans=="y" or ans=="Y":
        choose=int(input("enter your choice:\n1.data entry \n2.read data\n3.delete data\n4.update data \n"))
        if choose ==1:
            eagain='y'
            while eagain=="y" or eagain=="Y":
                eid=int(input("Enter the id number"))
                ename=input("Enter the name")
                cur=x.cursor()
                cur.execute("insert into emp values({},'{}')".format(eid,ename))
                x.commit()
                print("Data inserted successfully")
                eagain=input("Do you want to insert more data?")
        if choose==2:
            cur=x.cursor()
            cur.execute("select* from emp;")
            head=['Eid','Ename']
            data=cur.fetchall()
            print(tabulate(data,head,tablefmt='psql'))
            #for i in data:
             #   print(i)
            x.commit()
        if choose==3:
            eagain="y"
            while eagain=="y" or eagain=="Y":
                n=int(input("enter the eid to be deleted:"))
                cur=x.cursor()
                cur.execute("delete from emp where eid={}".format(n))
                x.commit()
                print("The diven data is deleted sucessfully")
                eagain=input("Do you want to delete more data?")
        if choose==4:
            cur=x.cursor()
            eagain="y"
            while eagain=="y" or eagain=="Y":
                chooser=int(input("choose data to update:\n1.eid\n2.ename\n"))
                if chooser==1:
                    oldid=int(input("enter the existing id:"))
                    newid=int(input("enter the new id:"))
                    cur.execute("update emp set eid={} where eid ={}".format(newid,oldid))
                    x.commit
                    print("data updated sucessfully")
                if chooser==2:
                    old=input("enter the existing  ename:")
                    new=input("enter the new ename:")
                    cur.execute("update emp set ename='{}' where ename='{}'".format(new,old))
                    
                    x.commit
                    print("data inserted sucessfully")
                eagain=input("do you want to update more data?")
        ans=input("do you want to continue?")
x.close()
                    
                            
            
            
            
