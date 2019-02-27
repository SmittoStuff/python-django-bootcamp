mylist = ['big',1,'boi',2,'swag']
print(mylist[2])
print("Before reassignment: {}".format(mylist))
mylist[0] = "BIGGER"
print("After reassignment: {}".format(mylist))
list2 = ['x','y','z']
mylist.append(list2)
print(mylist)
mylist.extend(list2)
print(mylist)

# Popping
mylist = ['a','b','c']
item = mylist.pop()
print(mylist)
print(item)

# Nested Lists
mylist = [1,2,[3,4,5]]
print(mylist[2])
print(mylist[2][1])

# List comprehension
matrix = [[1,2,3],[4,5,6],[7,8,9]]
first_col = [row[0] for row in matrix]
print(first_col)
