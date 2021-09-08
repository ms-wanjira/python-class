# # from datetime import date
# # my_date = date(1996, 12,30)
# # print("Date passed as argument is", my_date)

# # TODAY DATE
# # from datetime import date
# # today = date.today()
# # print("Data components", today)

# # TIMEDELTA
# # from datetime import datetime, timedelta
# # ini_time_for_now = datetime.now()
# # print("initial_date", str(ini_time_for_now))

# # # calculating the future dates
# # # for two years
# # future_date_after_2yrs= ini_time_for_now + timedelta(days = 730)
# # future_date_after_2days =ini_time_for_now + timedelta(days = 2)
# # print('future_date_after_2yrs:', str(future_date_after_2yrs))
# # print('future_date_after_2days:', str(future_date_after_2days))

# from datetime import datetime, timedelta

# ini_time_for_now = datetime.now()

# print("initial_date", str(ini_time_for_now))

# new_final_time = ini_time_for_now +  timedelta(days = 2)

# print("new_final_time", str(new_final_time))

# print("Time difference:", str(new_final_time - ini_time_for_now))


# import datetime

# todays_date =datetime.date.today()
# print("Original date: ", todays_date)
# modified_date = todays_date.replace(year=1998)
# print("Modified date: ", modified_date)

import datetime

birthdate=datetime.date(1998,10,16)
enddate=datetime.date(2020,9,8)
time_difference =(enddate) - (birthdate)
age = time_difference
print(age)

# from datetime import date

# def calculateAge(birthDate):
#     today = date.today()
#     age=today.year - birthDate.year 
#     ((today.month, today.day) <(birthDate.month, birthDate.day))
#     return age
# print(calculateAge(date(1998, 10, 16)))


# from datetime import date

# def calculateAge(born):
#     today= date.today()
#     try:
#         birthday = born.replace(year = today.year)
#     except ValueError:
#         birthday = born.replace(year = today.year,
#         month = born.month + 1, day = 1)
#     if birthday > today:
#         return today.year - born.year -1
#     else:
#         return today.year -born.year
# print(calculateAge(date(1997, 2,3)), "years")

# from datetime import date
# def calculateAge(birthDate):
#     days_in_year =365
#     age = int((date.today() - birthDate).days /days_in_year)
#     return age
# print(calculateAge(date(1998, 10,16)), "years")
















