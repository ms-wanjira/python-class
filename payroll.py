# GROSS SALARY

salary=int(input("Enter basic salary: "))
benefits1=int(input("Enter housing allowance-1: "))
benefits2=int(input("Enter food allowance -2: "))
benefits3=int(input("Enter benefit allowance-3: "))
benefits=benefits1 + benefits2 +benefits3
def gross_salary(x, y):
    z=x + y
    return z
gross= gross_salary(salary,benefits)
print("gross:", gross)

# NSSF
# def nssf(gross):

#    x=gross
def nssf(x):
    if x <18000:
      y= x * 0.06
    else:
      y= 1080
      return y
nssf= nssf(gross)
pension=gross-nssf
print("pension:", pension)

# payee
# payee=((pension)*%)

# x=pension


def payee (x):
    if x >24000 and x < 32333:
       y= 2400 + (x - 24000) * 0.25
    elif(x >32333):
       y= 2400 + 2083 + (x - 32333) * 0.3
    else:
        y=x * 0.1
    return y
payee=payee(pension)
print("payee", payee)
taxable_income=pension - (payee)
print("taxable_income", taxable_income)
        



    
