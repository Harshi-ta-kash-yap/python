from math import *
print("hello world")
a = 78
# + cancatinate string  and ,concatinate string as well as int
name = "ITRTIGJ"
print(name.islower())
# print("wellcome"+a+"my name", a)#+show error

print(name.lower().islower())
print(len(name))
print(name.replace('T', 'o'))

num = 465
# num uses in num2 as string  so we can concatinate with + symbol
num2 = str(num)
print(20 % 6)
print('number is '+num2)

print(abs(-353.878))  # absolute means ignore negative sign
print(max(4, 232))
print(bin(353))
# using math library
print(sqrt(25))

# input from user
name = input('input your name ')
age = int(input("your age "))
print('your name is '+name+' and your age ', age)

# repalce
word = input('Enter your sentences  ')
w1 = input('word which you wont to replace ')
w2 = input('word which you wont to put ')
print(word.replace(w1, w2))


list in python
h = 3553
h = 'bdjkfihgfng'  # <class 'str'>
h = 'j'  # <class 'str'>

country = ['india ', 'nepal', 'ihj', 'rassia']
print(country[1])
print(country[-2])
print(country[1:])
print(country[:4])
print(type(country))
print(type(h))
print(len(country))

fruit = ['apple', 'Mango', 'Orange ', 'apple', "apple", 'Banana', 'Lichi']
country.extend(fruit)  # 9
print(fruit)
print(len(country))
fruit.append('cherry')  # add element to last
print(fruit)
country.extend(fruit)  # copy element of list  to last
print(len(country))
country.insert(2, 'myyyys')  # add element in desired location
country.remove('ihj')  # remove
print(fruit.index('apple'))  # display  index
print(fruit.count('apple'))  # display no repeat element
fruit.sort()
fruit.reverse()
print(fruit)

# function declarationn


def create(name, age):
    print("Your name is  " + name+" and age is "+str(age))


name = input("Enter your name ")
age = input("Enter your age ")
create(name, age)


# if else statement practice
a = 9
b = 9
if a == b and b == 9:
    print("both are same ")

elif a == 0 or a == 8:
    print("value of a is 0 or 8  ")
else:
    print("both are not same ")
