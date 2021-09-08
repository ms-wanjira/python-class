# a date has day 'd' ,month
# 'm' and year 'y'

# from datetime import date


# class Date:
#     def _init_(self, d,m, y):
#        self.d =d
#        self.m =m
#        self.y =y

# # to store number of days from janua
# monthDays =[31,28,31,30,31,30,
# 31,31,30,31,30,31]

# # this function counts the number of leap years before the date given.
# def countLeapYears(d):
    
#     years = d.y

# # check if the current year needs 
# # be considered for the count
# # of leap years or not

# if (d.m <=2):
# years -= 1

# # a year is a leap year if it is a
# # mutilple of 4, mutiple of 400
# # and not a mutilple of 100

#  return int(years / 4) - int(years / 100) + int(years / 400)

# #  this functions returns number of days between
# # two given dates
# def getDifference(dt1, dt2):
#     # count number of days before first date 'dt1'

# # initialize count using years and days

# n1 = dt1.y * 365 + dt1.d

# # Add days for months in given date
#  for i in range(0, dt1.m -1):
#       n1 += monthDays[i]

# # since every leap yearis of 366 days,
# # add a day for every leap year

# n1 += countLeapYears(dt1)

# # simailarly,count total number of days before "dt2"

# n2 = dt2.y * 365 + dt2.d
# for i in range(0, dt2.m -1):
#     n2 += monthDays[i]
# n2 += countLeapYears(dt2)

# return (n2 -n1)

# dt1 = Date(8, 19,2021)
# dt2 = Date(16,10,1998)

# print(getDifference(dt1, dt2), "days")

# from datetime import datetime
# date_format = "%m/%d/%Y"
# a = datetime.strptime('8/18/2008', date_format)
# b = datetime.strptime('9/26/2008', date_format)
# diff = b - a
# print (diff.days)

