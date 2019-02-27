print(1 == 1)
print(1 == "1")
print((1 > 2) and (2 < 3))
print((1 > 2) or (2 < 3))

if 4<20:
 print("beast!")

# if, elif, else
if 1>2:
  print("beast")
elif 2>3:
  print("mode")
else:
  print("swag")

seq = [1,2,3,4,5,6]
for item in seq:
  print(item)

# Tuple Unpacking
mypairs = [(1,2),(3,4),(5,6)]
for (tup1,tup2) in mypairs:
  print(tup1)
  print(tup2)

# Range
for i in range(0,20,2):
  print(i)

# List Comprehension
x = [1,2,3,4]
out = [num**2 for num in x]
print(out)
