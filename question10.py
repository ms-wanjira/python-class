
# from datetime import datetime
# date_format = "%m/%d/%Y"
# a = datetime.strptime('10/16/1998', date_format)
# b = datetime.strptime('9/8/2021', date_format)
# diff = b - a
# print (diff.days)

import datetime
date=int(input("enter date"))
month=int(input("enter month: "))
year=int(input("enter year: "))
dob = datetime.datetime(year,month,date)
days = datetime.datetime.now() - (dob)
print(days)







































