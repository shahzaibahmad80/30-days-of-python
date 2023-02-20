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

