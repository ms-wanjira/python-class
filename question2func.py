# try again better function and code readability
# the same code? yeah

def my_list():
    a=list(range(0,50,5))
    # b=a[0::4]
    return a[0::4]
print(my_list())

# won't work because the function does not take any args
# so alos in the def we cant put the  range?
# think how can we make it shorter and avoid repetition
# i could have put the index in print 
# also try list(range(0,30,5))
# 5 specifies the interval
# instead of 5 10,15 20,25?
# yeah it makes work easier 
# ok let me do it with range....

# still bringing an errror
# so even in print you should also the function part()?
# yeah and if there's an argument you pass it
# now index
# what you want to do is create another variable and index awhy?

# we cant have two returns? no
# why?
