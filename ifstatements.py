# x = input("Enter a number ")
# print(type(x))


# y = input("Enter Marks")
# print(y)

# z = int(float(y))
# print(z)

# if z >= 0 and z <= 100:
#     print("Pass")
# else :
#   print("Fail")

x = float(input("Enter number "))
y = float(input("Enter a number "))
z = float(input("Enter a number"))

if (x == y == z) :
  print(" All are equal")
elif (x > y) and (x > z):
  print("x is the largest")
elif (y >x) and (y > z):
  print("y isthe largest")
elif (z >x) and (z > y):
  print("z isthe largest")
elif (y == z) and (y ==z):
  print("x and y are large")
elif(z==y) and (z >y):
  print("z and y are large")
else:
  print("Invalid")












