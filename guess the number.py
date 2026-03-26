import random as r
number=r.randint(1,10)
while True :
    guess=int(input())

    if guess<number:
        print("very low")
    elif guess>number:
        print("very high")
    elif guess==number:
        print("you got it, congractulations")
        break
'''above one is to not run the code again and again and can get answer by just one run'''

import random as r
number=r.randint(1,20)
guess=int(input())
if guess==number:
    print("congrats")
else:
    print("sorry, try again!!!")
'''this above one is for to run again and again'''
    
