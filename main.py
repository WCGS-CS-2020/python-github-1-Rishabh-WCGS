# Task One
#
#Create a function that, given a number, returns the corresponding Fibonacci number.
#
#Examples
#fibonacci(3) ➞ 3
#fibonacci(7) ➞ 21
#fibonacci(12) ➞ 233
#Notes
#The first number in the sequence starts at 1 (not 0).


def fibonacci (x) :
    s = 0
    t = 1
    i = 0
    print(s)
    while i < x:
        r = s
        s = t
        t = r + t
        i = i + 1
    print(s)  
    
print ("3rd Fibonacci number is: ", fibonacci(3))
print ("7th Fibonacci number is: ", fibonacci(7))
print ("12th Fibonacci number is: ", fibonacci(12))




# 
# Test your code there

# print ("3rd Fibonacci number is: ", fibonacci(3))
# print ("7th Fibonacci number is: ", fibonacci(7))
# print ("12th Fibonacci number is: ", fibonacci(12))

def join_digits (x) :

  joinstring = ""
  #
  # Fill in your code below

  return joinstring


# 
# Test your code there

test = [4, 11, 15]
for x in test :
  print ("join_digit: ", x, "is: ", join_digits (x))


#
# Task 3
#

#Create a function that returns the amount of duplicate characters in a string. It will be case sensitive #and spaces are included. If there are no duplicates, return 0.
#
#Examples
#duplicates("Hello World!") ➞ 3
#duplicates("foobar") ➞ 1
#duplicates("helicopter") ➞ 1
#duplicates("birthday") ➞ 0
# If there are no duplicates, return 0

# 
# Task 4
#

#A Primorial is a product of the first n prime numbers (e.g. 2 x 3 x 5 = 30). 2, 3, 5, 7, 11, 13 are prime #numbers. If n was 3, you'd multiply 2 x 3 x 5 = 30 or Primorial = 30.
#
#Create a function that returns the Primorial of a number.
#Examples
#primorial(1) ➞ 2
#primorial(2) ➞ 6
#primorial(8) ➞ 9699690

