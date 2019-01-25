from math import sqrt
########## Dynamic Input ################
num1String = input('Please enter an integer: ')
num2String = input('Please enter a second integer: ')

########## Part 1 - Reversing a Number##########
rev = num1String[::-1]
print('The original number is :',num1String)
print('The number obtained by reversing the digits is:',rev)

num1 = int(num1String)
num2 = int(num2String)

################## Part 2 - Arithmetic Operations ####################

print('The sum of square root of the two numbers is',sqrt(num1)+sqrt(num2))
print (num1,' plus ',num2,' equals ',num1+num2)
print (num1,' multiplied by ',num2,' equals ',num1*num2)
print (num1,' divided by ',num2,' equals ',num1/num2)
print (num1,' is greater than ',num2,' by ',num1-num2)


################ Part 3 - Identifying Letters, words and digits in a given string ############

saminp = "Python and Deep Learning CS 5590 5542"

words = len(saminp.split())
digits = sum(c.isdigit() for c in saminp)
letters = sum(c.isalpha() for c in saminp)

print('Number of digits in the string are:',digits)
print('Number of letters in the string are:',letters)
print('Number of words in the string are:',words)


print ('Thank you. END')