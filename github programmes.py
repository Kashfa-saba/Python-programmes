#USN,PASS=map(str,input().split())
#if USN=="Kashfa_saba" and PASS=="12345678":
#    print("verified")
#else:
#    print("not verified")

#USN=str(input())
#PASS=int(input())
#if USN=="Kashfa_saba" and PASS==12345678:
#    print("verified")
#else:
#    print("not verified")

units= float(input())
if units<=100:
    print(units*5)
elif units>100 and units<=200:
    print(units*7)
elif units>200 and units<=500:
    print(units*10)
else:
    print("enter valid units")
