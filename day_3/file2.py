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