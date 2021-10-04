# email=str(input("Enter Email Adress: "))
phonenumber=str(input("Enter Phonenumber: "))
nameofperson=(input("Enter Name: "))
empty = []


# def email_validator(x):
#     w=0
#     y=len(x)
#     dot = x.find(".")
#     at = x.find("@")
#     for i in range (0, at):
#       if ((x[i]>= 'w' and x[i]<='z') or (x[i]>='A' and x[i]<='Z')):
#        w=w+1
#     if(w >0 and at>0 and (dot-at)>1 and (dot + 1)<y) or(dot -1)>y:
#       empty.append(x)
#       # print("the email is valid")
#     else:
#       print("the email is invalid")
#     return(x)
# email_validator= email_validator(email)
# print("email_validator:",email )
# print(empty)
#This is what i did

def valid_email():
    while True: # I used the while loop so that it can prompt the user 
    #to enter a valid email address every time the user enters an input that is not valid
    # let me confirm if it will work
        email_address = input('Enter your email address: ')
        at_sign = email_address.find('@')
        dot = email_address.find('.')
        #The find() method returns the index of first occurrence of the substring (if found). 
        #If not found, it returns -1.
        # the while loop means that the email will keep typing?
        
        if at_sign != -1 and dot != -1:
            break
        else:
            print('Please enter a valid email address')
            continue
    return email_address

# what if we put the argument as email_address ?
# ?
# valid_email()

# try again

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
# phonenumber=str(input("Enter Phonenumber: "))

phone_num(phonenumber)
# print("phonenumber:-", phone_num)

def name(x):

  y=any(map(str.isdigit, x))
  if y is True:
    return 'enter valid name'
  else:
    return nameofperson
name=name(nameofperson)
print("name" ,name)


#Adding the results to a list
details = [valid_email(),phone_num,name]
print(details)

#try running again
# ITS BRINGING AN ERRO
# how do you run files on vs code
# below the minimize button there is a play button...press it
