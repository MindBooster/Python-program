 #percentage of boards CBSE science1
print("Enter the following details of student:-")
name=input("NAME:")
standard=int(input("CLASS:"))
rollno=int(input("ROLL NO:"))
print("enter marks of the following subjects:")
e=float(input("English:"))
p=float(input("Physics"))
c=float(input("Chemistry"))
cs=float(input("Computer Science"))
m=float(input("Maths"))
pe=float(input("Physical Education"))
sum=e+p+c+cs+m+pe
min=pe
if cs<min:
    min=cs
if m<min:
    min=m
if p<min:
    min=p
if c<min:
    min=c
TM=sum-min
per=(TM/500)*100
print("\t\t\tSBOA PUBLIC SCHOOL\t\t\t\n")
print("\t\t\t\tREPOT CARD\t\t\t\n")
print("NAME:",name,"\n\nCLASS:",standard,"\n\nROLL NO:",rollno\n)
print("SUBJECTS\t\tMARKS OBTAINED\n")
print("English\t\t\t",e)
print("Physics\t\t\t",p)
print("Chemistry\t\t",c)
print("Computer science\t",cs)
print("Maths\t\t\t",m)
print("Physical education\t",pe)
print("TOTAL MARKS OBTAINED:",TM)
print("TOTAL MARKS :500")
print("PERCENTAGE:",per,"%")


#sci_file=open("C:\\Users\\Hp\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages\\RAM\\science\\ins_science.txt","a+")


