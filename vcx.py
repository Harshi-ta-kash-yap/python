x = 5
y = 10
print(x + y)
print("jdfgyuegfugfjb  eurguifudjfkn egrugej\n\n")
d=abs(-38.96794)
a=abs(3 + 3 /758665*678)
assc=ascii(658)
print(d ,a ,assc)


print("\t\n\n\t\t\tTask 1 \n\nTwinkle, twinkle, little star,\n\tHow i wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are\n")

import sys
print("\n\t\tTsk2\nPython version",sys.version)
print("\n\nVersion info ",sys.version_info)

import datetime
now = datetime.datetime.now()
print("\n\t\tTasks3\n Current Date time : "+ now.strftime("%Y-%m-%d %h:%m:%S"))

from math import pi
r= float(input("\n\t\t Task 4\nInput the radius of the circle  = "))
print("area of circle with radius "+ str(r)+" is : " + str(pi*r**2))

f=input("\n\t\tTask5\n\nEnter First name ")
l=input("Last name ")
print("Hello "+ l+" "+f)

v=input("\n\t\tTask6 \nEnter elements separated by comma :")
list=v.split(",")
tuple=tuple(list)
print("list=  ",list)
print("tuple= ",tuple)

filename=input("\n\t\t Task7 \nEnter file name")
fe=filename.split(".")
print("the extention of file=== "+(fe[-1]))











