# prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]

prods = [['omo', '30ksh', 300], ['milk', '50ksh', 200], ['bread', '45ksh',359], ['coffee','5ksh',79]]

def list(x):
    x= prods
    return x
list = list(prods)
print("Legnth of items: ", len(prods))

 
def index_sum(x):
    w = (x[0][2])
    v = (x[1][2])
    y = (x[2][2])
    z = (x[3][2])
    return w + v + y + z
index_sum = index_sum(prods)
print("sum of stock:", index_sum)


