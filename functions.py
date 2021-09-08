# def calculate(num1, num2):
#     t= num1 + num2
#     return t
# y = calculate(30)
# print(y)

# import datetime
# date=int(input("enter date"))
# month=int(input("enter month: "))
# year=int(input("enter year: "))
# dob = datetime.datetime(year,month,date)
# days = datetime.datetime.now() - (dob)
# print(days)

import datetime
def calculateage():
    x=int(input("enter date"))
    y=int(input("enter month: "))
    z=int(input("enter year: "))
    return(x,y,z)
b=calculateage()
print(type(b))

# ...............................................
# # current date
# def calculatedate():
#     n = datetime.datetime.now() 
#     return(n)
# m=calculatedate()
# print(m)






# dob = datetime.datetime(year,month,date)
# days = datetime.datetime.now() - (dob)
# print(days)