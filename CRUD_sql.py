import mysql.connector as ms
from tabulate import tabulate
import matplotlib.pyplot as plt
x=ms.connect(host="localhost",user="root",passwd="123",database="Student")
cur=x.cursor()
def plot_graph():
    cur.execute("select phy from Stu_info")
    data=cur.fetchall()
    physics_analysis=[]
    for row in data:
        physics_analysis.append(row[0])
    plt.plot(physics_analysis)
    plt.show()
if x.is_connected():
    ans='y'
    while ans=='y' or ans=='Y':
        chooser=int(input("Enter your choice:\n1. Student Data Entry (C)\n2.Read Data (R)\n3.Update Data (U)\n 4. Delete Data (D)\n"))
        if chooser==1:
            e_again='y'
            while e_again=='y' or e_again=='Y':
                cur=x.cursor()
                roll=int(input("Enter Roll No: "))
                name=input("Enter Student Name: ")
                print("Enter Marks in the following subjects:")
                phy=float(input("Physics: "))
                che=float(input("Chemistry: "))
                maths=float(input("Maths: "))
                sql_q="insert into Stu_info values({},'{}',{},{},{})".format(roll,name,phy,che,maths)
                cur.execute(sql_q)
                x.commit()
                print("Data inserted successfully")
                e_again=input("Do you want to insert more data ?(y/n)")
        if chooser==2:
                cur=x.cursor()
                sql_q="select * from Stu_info"
                cur.execute(sql_q)
                data=cur.fetchall()
                headers=['Roll','Name','Physics','Chemistry','Maths']
                print(tabulate(data,headers,tablefmt='psql'))
                #for i in data:
                 #   print(i)
        if chooser==3:
                e_again='y'
                while e_again=='y' or e_again=='Y':
                        cur=x.cursor()
                        update_chooser=int(input("Choose Data to Update\n 1. Update Roll No \n 2. Update Name \n 3. Update Marks\n"))
                        if update_chooser==1:
                            ex_roll=int(input("Enter existing Roll Number:"))
                            new_roll=int(input("Enter new Roll Number: "))
                            sql_q="update Stu_info set roll={} where roll={}".format(new_roll,ex_roll)
                            cur.execute(sql_q)
                            x.commit()
                            print("New Roll Number Updated Successfully")
                        if update_chooser==2:
                            roll=int(input("Enter Roll Number:"))
                            new_name=input("Enter new name: ")
                            sql_q="update Stu_info set name='{}' where roll={}".format(new_name,roll)
                            cur.execute(sql_q)
                            x.commit()
                            print("name updated successfully")
                        if update_chooser==3:
                            a="y"
                            while a=='y' or a=='Y':
                                sub_chooser=int(input("Which subject marks fo you want to update ? \n Press \n1. Physics \n 2. Chemistry \n 3.Maths \n"))
                                if sub_chooser==1:
                                    roll=int(input("Enter Roll Number:"))
                                    phy=float(input("Enter new marks of Physics: "))
                                    sql_q="update Stu_info set phy={} where roll={}".format(phy,roll)
                                    cur.execute(sql_q)
                                    x.commit()
                                    print("Marks updated successfully")
                                if sub_chooser==2:
                                    roll=int(input("Enter Roll number:"))
                                    chem=float(input("Enter the marks of chemistry:"))
                                    sql_q="update Stu_info set che={} where roll={}".format(chem,roll)
                                    cur.execute(sql_q)
                                    x.commit()
                                    print("Marks updated successfully")
                                if sub_chooser==3:
                                    roll=int(input("Enter Roll number:"))
                                    maths=float(input("Enter the marks of maths:"))
                                    sql_q="update Stu_info set maths={} where roll={}".format(maths,roll)
                                    cur.execute(sql_q)
                                    x.commit()
                                    print("Marks updated successfully")
                                a=input("Update Another Marks ? (y/n)")
                        e_again=input("Update More Data ? (y/n)")
        if chooser==4:
                    a='y'
                    while a=='y' or a=='Y':
                        cur=x.cursor()
                        roll=int(input("Choose Roll Number to delete: "))
                        sql_q="delete from Stu_info where roll={}".format(roll)
                        cur.execute(sql_q)
                        x.commit()
                        print("Data of Roll No: {} deleted successfully".format(roll))
                        a=input("Delete more data ?(y/n)")
        ans=input("Do you want to continue(y/n)?")
plot_graph()
print("Thank you for using our application")                         
x.close()
