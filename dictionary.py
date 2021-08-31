# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }

# # print(thisdict)

# thisdict["model"] = "Ford"

# # print(thisdict)

# print(thisdict.clear())
# print(thisdict.copy())

# thisisdict = {}.fromkeys

# Dictionary Methods
# marks = {}.fromkeys(['Math', 'English', 'Science'], 0)

# # Output: {'English': 0, 'Math': 0, 'Science': 0}
# print(marks)

# for item in marks.items():
#     print(item)

# # Output: ['English', 'Math', 'Science']
# print(list(sorted(marks.keys())))

# taskList = [23, “Jane”, [“Lesson 23”, 560, {“currency” : “KES”}], 987, (76,”John”)]
# Determining type of variable in  taskList using an inbuilt function
# Print KES
# Print 560
# Use a function to determine the length of taskList
# Change 987 to 789 without using an inbuilt -method or Assignment
# Change the name “John” to “Jane” .



tasklist = [23, "Jane", ["Lesson 23", 560, {"currency" : "KES"}], 987, (76,"John")]
# print(type(tasklist))
# print(tasklist[2])
# print(tasklist[2][2]["currency"])
# print(tasklist[2][1])
# print(len(tasklist)
tasklist[3] = str(tasklist[3])
tasklist[3] = int(str(tasklist[3][::-1]))
print(tasklist)


# y= tasklist
# y.reverse([3])
# print(y)



# tasklist= [23, "Jane", ["Lesson 23", 560, {"currency" : "KES"}], 987, (76,"John")]

# tasklist[4]=list(tasklist[4])
# tasklist[4][1] = "Jane"
# tasklist[4]= tuple(tasklist[4])

# print(tasklist[4])

# tasklist[4]=(76,"jane")
# print(tasklist[4])
















