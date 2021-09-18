# QUESION TWO
# a = [5,10,15,25]
# print(a[0::3])

def check_even():
    a=list(range(0,100))
    for i in a:
        if i % 2 == 0:
            return(i, "Num is even") 
        else:
            return("pass")
print(check_even())