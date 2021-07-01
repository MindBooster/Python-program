def determine (s):
    d={"upper":0,"lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("original string:",s)
    print("upper case count:",d["upper"])
    print("lower case count:",d["lower"])
determine("These are Happy Times")
