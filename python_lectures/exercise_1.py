# Indexing
s = 'django'
# d
print(s[0])
# o
print(s[-1])
# djan
print(s[:4])
# jan
print(s[1:4])
# go
print(s[4:])
# reverse the string
s[::-1]

# Set hello to be goodbye
l = [3,7,[1,4,'hello']]
l[2][2] = 'goodbye'
print(l)

# Grab 'hello' from dictionaries
d1 = {'simple_key': 'hello'}
print(d1['simple_key'])
d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])

# Use set to find unique values
mylist = [1,1,1,1,1,2,2,2,2,3,3,3]
print(set(mylist))

# Use print formatting
print("hello my beast's name is {a} and he is {b} years old".format(a='tony',b='beast'))
