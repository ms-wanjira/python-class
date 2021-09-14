# GROSS SALARY

salary=int(input("Enter basic salary: "))
benefits1=int(input("Enter housing allowance-1: "))
benefits2=int(input("Enter food allowance -2: "))
benefits=benefits1 + benefits2
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


# NHIF
def nhif(x):
    if (x > 5999):
        y = 150
    elif x > 6000 and x<7999:
        y = 300
    elif x > 8000 and x<11999:
        y = 400
    elif x > 12000 and x <14999:
        y = 500
    elif x > 15000 and x<19999:
        y =600
    elif x > 20000 and x<24999:
        y = 750
    elif x <25000  and x<29999:
        y =850
    elif x > 30000  and x< 34999:
        y = 900
    elif x > 35000 and x< 39999:
        y= 950
    elif x >40000  and x< 44999:
        y= 1000
    elif x >45000  and x<49999:
        y=1100
    elif x >50000  and x<59999:
        y=1200
    elif x >60000  and x< 69999:
        y=1300
    elif x > 70000 and x<79999:
        y=1400
    elif x > 80000 and x<89999:
        y=1500
    elif x > 90000 and x<99999:
        y=1600
    else:
        y=1700
    return y
nhif=nhif(gross)
print("nhif:", nhif)


def net_pay():
    x= nhif
    y=nssf
    z=payee
    w= x+y+z
    return w
deductions=nhif + nssf + payee
print("deductions:", deductions )
net_pay= gross - (deductions)
print("net_pay: ", net_pay)



    
