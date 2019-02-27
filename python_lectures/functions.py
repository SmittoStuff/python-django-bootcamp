def my_func(param1='default'):
  print("This function is {a}!".format(a=param1))

my_func("beast")

def add_num(num1,num2):
  if type(num1) == type(num2) == type(10):
    print(num1+num2)
  else:
    print("We need INTS!!")

add_num(1,2)
add_num("1",2)

# Lambda expression
mylist = [1,2,3,4,5,6,7,8]
evens = filter(lambda num: num%2 == 0,mylist)
print(list(evens))

# Splits
tweet = "Go Sport! #Normies"
result = tweet.split("#")[1]
print(result)

# In
print('x' in [1,2,3])
