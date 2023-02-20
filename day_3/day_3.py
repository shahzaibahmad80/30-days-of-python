age = 21
height = 5.4
c = 1 + 2j

base = int (input("Enter the base:  ")) 
height = int (input("Enter the height:  "))
area = 0.5 * base *height
print("the area of triangle is: ",  area)

a = float (input("Enter side a: ")) 
b = float (input("Enter side b: ")) 
c = float (input("Enter side c: ")) 
perimeter = a+b+c
print("the perimeter of the triangle is:  ", perimeter)

length  = int (input("Enter the length:  ")) 
width = int (input("Enter the width:  "))
area1 = length * width
perimeter1 = 2 * (length * width)
print("the area1 of triangle is: " , area1)
print("the perimeter1 of triangle is: " , perimeter1)

radius = float(input("Enter the raidius of a circle: "))
pi = 3.1415
area2 =  pi * radius * radius
circumference = 2 * pi * radius
print("Area2 of circle is: " , area2)
print("circumference of circle is: " , circumference)


equation = "y = 2x - 2"
m = 2
b = -2
x_intercept = -b/m
print("Slope: ", m)
print("Y-intercept: ", b)
print("X-intercept: (", x_intercept, ", 0)")

import math
x1, y1 = 2, 2
x2, y2 = 6, 10
m = (y2 - y1) / (x2 - x1)
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Slope: ", m)
print("Euclidean distance: ", d)

x = float (input("Enter the value of x:  ")) # x = -3 will give the value of y as zero.
y = x**2 +6*x + 9
print("The value of y is : ", y )

if len("python") != len("dragon"):
    print("Length is not equal ")
else:
    print("Length is equal")

print("does the word on exist in python or dragon:", 'on' in 'python' and 'on' in 'dragon')

a= "I hope this course is not full of jargon"
print("Does the word jargon exist in above given sentence: ","jargon" in a)

print("does the word on exist in python or dragon:")
print(not('on' in 'python' and 'on' in 'dragon'))

b = 'python'
l = len(b)
print('length of this word is: ', l)
value_to_float = str(l)
print('the data type of the value has been convert to string: ', type(value_to_float))

num = float (input("enter a number: "))
if (num%2 == 0):
    print("number is even")
else:
    print("number is odd")

a = 7
b = 3
c = a//b
print("floor div is : ", c)
print("type: ", type(c))

d = '10'
e = 10
if(type(d) and type(e)): 
    print('both have same type: ')
else:
    print('they have no same type: ')

a = float('9.8')
if a == 10:
        print("a is equal to 10.")
else:
        print("a is not equal to 10.")

hour =int (input('enter hours: '))
rate_per_hour =int (input('enter rate: '))
pay = hour* rate_per_hour
print("total pay per hour is: ", pay)

years =int (input('enter number of years you have lived: '))
seconds_in_year = 60 * 60 * 24 * 365

lived_seconds = years * seconds_in_year
print("you have lived for ", lived_seconds, "seconds")

print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
