def printit(list1):
    m=n=list1[0]
    for a in list1:
        if a<n:
            n=a
        if a>m:
            m=a
    print("biggest",m,"smallest",n)
list1=[2,13,11,15,6]
printit(list1)
