email=str(input("Enter Email Adress: "))
phonenumber=str(input("Enter Phonenumber: "))
nameofperson=(input("Enter Name: "))
empty = []

def email_validator(x):
    w=0
    y=len(x)
    dot = x.find(".")
    at = x.find("@")
    for i in range (0, at):
      if ((x[i]>= 'w' and x[i]<='z') or (x[i]>='A' and x[i]<='Z')):
       w=w+1
    if(w >0 and at>0 and (dot-at)>1 and (dot + 1)<y) or(dot -1)>y:
      empty.append(x)
      # print("the email is valid")
    else:
      print("the email is invalid")
    # return(x)
email_validator= email_validator(email)
# print("email_validator:",email )
print(empty)
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
  if y is True:
    return 'enter valid name'
  else:
    return nameofperson
name=name(nameofperson)
print("name" ,name)


# def details(y):
#   x=Nameofperson
#   n=email
#   z=phone_num
#   y=x,n,z
#   return (y)
# details = details()
# print('list: ', details)
# for i in range(len(details)):
#     details[i] = int(details[i])


# def add_to_list():
#   empty_list = [email_validator,phone_num,name]
  
#   return empty_list

# print(add_to_list())
