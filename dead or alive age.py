age=int(input())
if(age<0):
    print("unborn")
elif(age>=1 and age<=5):
    print("new born")
elif(age>=15 and age<20):
    print("teenager")
elif(age>=20 and age<=50):
     print("adult")
elif(age>=51 and age<=90):
    print("senior citizen")
else:
    print("dead")
