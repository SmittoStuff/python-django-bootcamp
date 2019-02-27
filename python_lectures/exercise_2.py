# Given a list of integers, return True if the sequence 1,2,3 appears in the list somewhere
def arrayCheck(nums):
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and num[i+2]==3:
      return True
  return False

# Given a String, return a ne String made of every other character starting with the first,
# so "Hello" yields "Hlo"
def stringBits(mystring):
  result = ""
  for i in range(len(mystring)):
    if i%2 == 0:
      result = result + mystring[i]
  return result

# Given two Strings, return True if either of the Strings appears at the very end of the other String
def end_other(a,b):
  a = a.lower()
  b = b.lower()
  # return(b.endswith(a) or a.endswith(b))
  return a[-len(b):] == b or a == b[-len(a):]

# Given a String, return a String where for every char in the original, there are two chars
def doubleChar(mystring):
  result = ''
  for char in mystring:
    result += char*2
  return result

# Given 3 int values, a,b,c, return their sum. However, if any value is in the range (13-14,16-19) that counts at 0
def no_teen_sum(a,b,c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
  if n in [13,14,17,18,19]:
    return 0
  return n

# Return the number of even Integers in the given Array
def count_evens(nums):
  count = 0
  for num in nums:
    if num%2 == 0
      num_even += 1
  return num_even
