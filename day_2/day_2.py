#Day 2: 30 Days of python programming
first_name='Shahzaib'
last_name='Ahmad'
full_name='ali ahmad'
country= 'Pakistan'
city= 'multan'
age= 20
year= 2023
is_married= False
is_true= True
is_light_on= False
name,profession,hobby = 'ali','teaching','reading good books'

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))
print(type(is_true))
print(type(name))
print(type(profession))
print(type(hobby))

print(len(first_name))

if len(first_name)>len(last_name):
    print("First name is greater than last")
elif len(first_name)<len(last_name):     
    print("last name is greater than first")
else:
    print("both have same length")

num_one = 5
num_two = 4
total =num_one+num_two
print(total)

num_one = 5
num_two = 4
diff =num_one-num_two
print(diff)

num_one = 5
num_two = 4
division =num_one/num_two
print(division)

num_one = 5
num_two = 4
remainder =num_one%num_two
print(remainder)

num_one = 5
num_two = 4
exp =num_one**num_two
print(exp)

#5
r=30
area_of_circle = 3.14*r**2
print("area of circle is ",area_of_circle)

circum_of_circle = 2 * 3.14 * 30
print("circumference of circle is:", circum_of_circle )

rad = float(input("Enter the Area of a Circle:" ))

pi = 3.14159
area = pi * rad**2
print("Area of a Circle is: ", area)

first_name = input("Enter your first name:")
last_name = input("Enter your last name:")
country = input("Enter your country name:")
age  = input("Enter your age:")

help('keywords')