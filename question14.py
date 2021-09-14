email=str(input("Enter Email Adress: "))
phonenumber=str(input("Enter Phonenumber: "))
Nameofperson=(input("Enter Name: "))

def email_validator(x):
    w=0
    y=len(x)
    dot = x.find(".")
    at = x.find("@")
    for i in range (0, at):
      if ((x[i]>= 'w' and x[i]<='z') or (x[i]>='A' and x[i]<='Z')):
        w=w+1
    if(w >0 and at>0 and (dot-at)>1 and (dot + 1)<y) or(dot -1)>y:
      print("the email is valid")
    else:
      print("the email is invalid")
    return(x)
email_validator= email_validator(email)
print("email_validator:",email )


def phone_num(x):  
    if x[0:2] == "07":
        y = "+254" + x[1:]
    elif x[0:2] =="71":
        y = "+254" + x[0:]
    elif x[0:2] =="01":
        y = "+254" + x[1:]
    elif  x[0:3] == "254":
        y = "+254" + x[3:]
    print(y)
    return(y)
phone_num=phone_num(phonenumber)
print("phonenumber:-", phone_num)

def name(x):
  y=any(map(str.isdigit, x))
  return y
name=name(Nameofperson)
print("name" ,name)


def details(y):
  x=Nameofperson
  n=email
  z=phone_num
  y=x,n,z
  return (y)
details = details()
print('list: ', details)
for i in range(len(details)):
    details[i] = int(details[i])






