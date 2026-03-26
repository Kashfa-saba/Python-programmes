units= float(input())
if units<=100:
    print(units*5)
elif units>100 and units<=200:
    print(units*7)
elif units>200 and units<=500:
    print(units*10)
else:
    print("enter valid units")
