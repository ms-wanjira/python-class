email=str(input("Enter Email Adress: "))
# phonenumber=int(input("Enter Phonenumber: "))
# Nameofperson=(input("Enter Name: "))

def email_validator(x):
    if ("@") in x and (".com") in x:
      y= "valid email"
    else:
        y= "invalid email"
        return y
email_validator=email_validator(email)
print("valid or not: ",email)
 


