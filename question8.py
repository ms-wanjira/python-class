# Question8
for number in range(1, 201):
    count= 0
# print(count)
    for i in range(2, (number//2 + 1)):
        if(number % i ==0):
            count=count + 1
            break

    if(count == 0 and number !=1):
       print("%d" %number, end= " ")
