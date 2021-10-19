# def connect(**files):
#     print(type(files))
#     print(files)
# connect()




# def connect(**kwargs):
#     print(kwargs)

# config = { 'server': 'localhost','port': 5505,'user': 'root','password':'python58'}

# connect(**config)


# def group_by_owners(**kwargs):
#     print(kwargs)
#     print([])

# files={'input.txt':'Randy', 'Code.py':'Stan', 'Output.txt':'Randy'} 

# group_by_owners(**files)



# rate={'Bob':"Excellent", "Barnum":"passing","Beatrice":"passing","ben":"no pass","belle":"Excellent","bill":"passing","bernie":"passing","baxter":"excellent"} 


# from collections import defaultdict
# grouper = defaultdict(list)
# for k,v in rate.items():
#     grouper[v].append(k)
# print(grouper)

# files = {
#         'Input.txt': 'Randy',
#         'Code.py': 'Stan',
#         'Output.txt': 'Randy'
#     } 
# # def group_by_owners():

# from collections import defaultdict
# grouper = defaultdict(list)
# for k,v in files.items():
#     grouper[v].append(k)
# print(grouper)



# Implement a group_by_owners function that:

# Accepts a dictionary containing the file owner name for each file name.
# Returns a dictionary containing a list of file names for each owner name, in any order.
# For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.


from collections import defaultdict

files={'input.txt': 'Randy', 'code.py':'Stan','output.txt':'Randy'}

def group_by_owners():
    grouper=defaultdict(list)
    for k,v in files.items():
        grouper[v].append(k)
    return grouper
print(group_by_owners())
   


            
