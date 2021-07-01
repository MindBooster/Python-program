import mysql.connector as ms
x=ms.connect(host="localhost",user="root",passwd="123",database="Sanjana")
if x.is_connected():
    cur=x.cursor()
    eid=int(input("Enter Employee ID to fetch information : "))
    cur.execute("select * from Emp where e_id={}".format(eid))
    data=cur.fetchall()
    for i in data:
        print(i)
    x.close()
    ''' y=cur.rowcount
    print("No of rows fetched so far: ",y)
    data=cur.fetchone()
    print(data)
    rc=cur.rowcount
    print("Row Count now:",rc)
    x.close()'''
