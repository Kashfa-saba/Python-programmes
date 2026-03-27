try:
    num=int(input("enter the nuber: ")
    result=10/num
    print("Result",result)
except ValueError:
    print("Invalid input! Please enter another number")
except ZeroDivisionError:
    print("cannot divided by zero")


'''-----EXCEPTIONAL HANDLING-----
This allows the program to detect the errors and respond appropriately and continue running'''
