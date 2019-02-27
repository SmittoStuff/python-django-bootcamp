mystring = 'abdcefg'
print(mystring[0])
uppercase = mystring.upper()
print(uppercase)

# Split
mystring = 'Hello World'
x = mystring.split()
print(x)
y = mystring.split('o')
print(y)

# Print Formatting
x = "Insert another string here: {}".format("BEAST!")
print(x)
x = "Item One: {x}, Item Two: {y}".format(x="Big", y="Boi")
print(x)
