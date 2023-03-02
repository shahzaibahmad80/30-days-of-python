a = 'Thirty'
b = 'Days'
c = 'Of'
d = 'Python'
space = ' '
Concatenated_Stirng  = a+space+b+space+c+space+d
print("So, the concatenated stirng is: ", Concatenated_Stirng )

e = 'Coding'
d = 'For'
f = 'All'
space = ' '
Concatenated_Stirng_0 = e+space+d+space+f
print("So, the concatenated stirng is: ", Concatenated_Stirng_0 )


company = "coding for all"
print("the printing variable is: ", company)
l = len(company)
print("the length is: ", l)
print(company.swapcase())
print(company.capitalize())
print(company.title())

cut = company[6:14]
print("after cutting the output will be : ", cut)
#Cut_First_Word = company.split('coding')
#print("After cutting first word output will be: ", Cut_First_Word)
firs_word = "coding for all"
#sub_sting = "coding"
#print(first_word.index(sub_sting))
print(firs_word.find('coding'))
print(firs_word.replace('coding','Python'))
print(firs_word.replace('coding for all', 'Python for everyone'))

print(firs_word.split(" \t"))
new_string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(new_string.split())

zero_index = company[0]
print("the chracter at zero index: ", zero_index) 
last_index = len(company) - 1
last_index = company[last_index]
print("the last character on the last index is: ", last_index)
tenth_index = company[10]
print("the chracter at 10th index: ", tenth_index) 

python_abv = "Pyhton For Everyone"
abv = " ".join("PFE")
print("The abbriviation for 'Pyhton For Everyone' is: ", abv)
coding_abv = 'Coding For All'
abv_1 = " ".join("CFA")
print("The abbriviation for 'Coding For All' is: ", abv_1)

#string_finding = 
#find_position = 'C'
#find_position = 'F'
#find_position = 'l'
#print(coding_abv.index(find_position))
#print(coding_abv.rindex(find_position))
#beacuse = 'You cannot end a sentence with because because because is a conjunction'
#find_because = 'because'
#print("the first occure of because is : ", beacuse.index(find_because)) #31_index
main_string = "You cannot end a sentence with 'because', 'because', 'because' is a conjunction"
print('first occurence of word "because" in the string: ', main_string.find('because'))
sub_string_b = 'be'
sub_string_e = 'is'
print(main_string.index(sub_string_b))
print(main_string.index(sub_string_e))


#find_because = 'because'
#print("the last occure of because is : ", beacuse.rindex(find_because)) #47_index
challenge = 'thirty days of pythoonnn'

print(challenge.strip('noth')) # 'irty days of py'


finding_SubString = "Coding for all"
print("Does this string end with substring 'Coding' ", finding_SubString.startswith('Coding') ) #28

print("Does this string end with substring 'Coding' ", finding_SubString.endswith('coding') )   #29

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
remove_space = '   Coding For All      '
trimmed_string = remove_space.strip()
print(trimmed_string)
#print("Removing the space:",remove_space.strip() )

#chech_identifier = '30DaysOfPython'
chech_identifier = 'thirty_days_of_python'
print (chech_identifier.isidentifier())

python_libraries =['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
hash = '# '.join(python_libraries)
print(hash)

print("I am enjoying this challenge.\nI just wonder what is next")

Data = "Name\tage\tcountry\tcity"
print(Data.expandtabs())

radius  = 10
area  = 3.14 * radius **2
area_of_a_circle = 'The area of circle with a radius %d is %.2f.' %(radius, area)
print(area_of_a_circle)  

a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')