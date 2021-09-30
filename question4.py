# QUESTION FOUR.



def phone_num():
    t = str(input("Enter a phone number "))
    if t[0:2] == "07":
        t = "+254" + t[1:]
    elif t[0:2] =="71":
        t = "+254" + t[0:]
    elif t[0:2] =="01":
        t = "+254" + t[1:]
    elif t[0:3] == "254":
        t = "+254" + t[3:]
    return t
print(phone_num())
