num=int(input("enter speed of car"))
if num <=70 :
    print("okay")
else:
    fastspeed= ((num -70)//5)
    if fastspeed <=12:
        print("Demerit points: " , fastspeed)
    else:
        print("Licence is suspended")
