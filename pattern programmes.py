n=int(input())
m=int(input())
for i in range(n,m,-2):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(n,m,2):
    for j in range(i):
        print("*",end=" ")
    print()
    
'''here n=the end range and the m is the starting point and if we take -2, we will get the output
as inverse triangle'''
'''n=18
  m=0 
* * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * 
* * * * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * 
* * * * * * 
* * * * 
* * '''
'''and here if we take n=0, m=18 while doing decrement of -2 we wont get the output, while we have
decrement the end range should be greater than start range'''
'''n=1(start range)
 m=8(end range)
* 
* * * 
* * * * * 
* * * * * * *, here the decrement loop didnt even run but the increment loop ran and gave us the pattern
of the odd number as it started with odd(1)'''
''' 


        
    
