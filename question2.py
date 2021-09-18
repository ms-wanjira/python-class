# QUESION TWO
# a = [5,10,15,25]
# print(a[0::3])

# def check_even():
#     a=list(range(0,100))
#     for i in a:
#         if i % 2 == 0:
#           return(i, "Num is even") 
#         else:
#           return(i, "pass")
# print(check_even())

# user_input = int(input('Enter number: '))
# def num():
#     x = user_input
#     if x % 2 == 0:
#         return( x, 'even number')
#     else:
#         return(x, 'odd number')
   
# print(num())



def num(n):
    if n % 2 == 0:
       return "even"
    else:
        return "odd"
# n= int(input("Enter number"))
# print(num(n))

# my_list = [5,10,15,20,25]
def my_list():
    a=[5,10,15,20,25]
    b=a[0::4]
    return b    
print(my_list())
