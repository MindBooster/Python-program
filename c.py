import random
STRING="CBSEONLINE"
NUMBER=random.randint(0,3)
N=9
while STRING[N]!="L":
    print(STRING[N]+STRING[NUMBER]+"#",end="")
    NUMBER=NUMBER+1
    N=N-1
    
