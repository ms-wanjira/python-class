def check():
    x = range(4)
    b=[]
    c=[]
    for i in x:
        user_input = int(input('Enter number: '))
        b.append(user_input)
    for i in b:
        if i not in c:
          c.append(i)
        y=max(c)
    return y
print(check())

# check_max()
