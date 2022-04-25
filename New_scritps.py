'''x=1
x>2
if x > 2:
    print('X is great than 2')
else:
    print('X is not great than 2')
print('Left program') '''

##for x in range (10):
##print(x)

##len("Fernanda")

'''def greet_someone(name):
    return f"Hello {name}!"
##greet_someone (name="Alex")'''

'''a= b= c= 300
print(a,b,c)'''

'''num = -3    
if num > 0:
    print('Positive number')
elif num == 0:
    print('Zero')
else:
    print('Negative number')'''

'''num = float(input('Enter a number: '))
if num >= 0:
    if num == 0:
        print('Zero')
    else:
        print('Positive number')
else:
    print('Negative number')'''

'''numbers = [5, 6, 7, 8, 9, 2, 15]
sum = 0

for val in numbers:
    sum = sum + val

print('The sum is', sum)'''

'''genre = ['pop', 'rock', 'jazz']
for i in range(len(genre)):
    print('I like', genre[i])'''

# program to display student's marks from record
'''student_name = 'Maria'

marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        #break
else:
    print('No entry with that name found.')'''

# To take input from the user,
'''n = int(input("Enter n: "))

# n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i + 1  # update counter

# print the sum
print("The sum is", sum)'''

'''counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")'''

# Use of break statement inside the loop

'''for val in "String":
    if val == "i":
        break
    print(val)

print("The end")'''

# Program to show the use of continue statement inside loops

'''for val in "tatiana banana":
    if val == "i":
        continue
    print(val)

print("The end")'''

## creating a function
'''def greet(): ##greet is name of the function
    print('Hello')
    print('How are you?')
greet()'''

'''def greet(name): ##greet is name of the function
    print('Hello', name)
    print('How are you?')
greet('Jose')'''

'''def add_numbers(n1,n2):
    result = n1 + n2
    print('The sum is:', result)

number1 = 4.6
number2 = 5.9
add_numbers(number1,number2)'''

'''def add_numbers(n1,n2):
    result = n1 + n2
    return result

number1 = 4.6
number2 = 5.9
result = add_numbers(number1,number2)
print('The sum is', result)'''


# function to find average marks
'''def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subjects = len(marks)  ## show how many items in the list
    average_marks = sum_of_marks / total_subjects
    return average_marks'''


'''marks = [55, 64, 75, 80, 65]
average_marks = find_average_marks(marks)
print('Your average mark is:', average_marks)'''


####Calculate the grade and return it

'''def compute_grade(average_marks):
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return grade


marks = [55, 64, 75, 80, 65]
average_marks = find_average_marks(marks)
print('Your average mark is:', average_marks)

grade = compute_grade(average_marks)
print('Your grade is:', grade)'''

## creating lists####################################################3
##numbers = ['Python', 'C++','sql','java']
##print(numbers[-1]) ## len quantity of items, which item of the list you want to print, if we put negative number
##like in the exemple,the last item of the list will be printed

'''numbers = ['Python', 'C++','sql','java','Asp', 'Oracle']
print(numbers[1:4]) # slice list,the first number refers to the position.the second refers to the elements, the last position
is not included'''

'''numbers = ['Python', 'C++','sql','java','Asp', 'Oracle']
print(numbers[:4]) ## the 4 elements will be printed
print(numbers[1:])## all elemnts will be displayed from the position 1'''
'''numbers = ['Python', 'C++','sql','java','Asp', 'Oracle']
print(numbers)
## changing the element in the position 1
numbers[1] = 'Cobol'
print(numbers)'''

#numbers = ['Python', 'C++','sql','java','Asp', 'Oracle']
'''print(numbers)
numbers[1:3]= ['Cobol', 'Pascal']
print(numbers)'''

#####verify if the item is in the list
##print('Rust' in numbers)


### add item in the list
'''numbers.append('Rust')
print(numbers)'''

## changing the position

'''numbers.insert(1,'java')
print(numbers)'''

###removing item from the list
'''numbers.remove('Oracle')
print(numbers)'''

###copying list

'''numbers1 = numbers.copy()
print(numbers1)
print(numbers)'''

##STRING###
'''text1 = 'Python'
text2 = 'programing'

result = text1 + " " + text2
print(result)'''

#### SET ###

'''animals = {'cat', 'tiger', 'lion', 'dog'}
print(animals)
print('tiger' in animals)'''

'''domestic_animals = {'cat', 'dog', 'elephant'}
wild_animals = {'lion', 'tiger', 'elephant'}

animals = domestic_animals.union(wild_animals)
print(animals)'''

#### DICTIONARY####################333
'''person1 = {'name':'luiz', 'age':'21'}  ### key the first,value the second
print(person1.get('hobbies')) ## item not in the dictionary'''

##print(person1['name'])

####changing the key

'''person1 = {'name':'luiz', 'age':'21'}
print(person1)

person1['name'] = 'Andre'
print(person1)'''

## add new key in the dictionary

'''person1['hobbies'] = ['dancing', 'fishing']
print(person1)

## removing item from a dictionary
person1.pop('name')
print(person1)

#####
for key in person1:
    print(key)'''

###
'''x = float(input('Enter a number: '))
if x > 2:
    print("X is more than 2")
    print("More text")
else:
    print("X isn't more than 2")
print("Left the condition")
'''


'''x = float(input('Enter a number: '))
my_var = 'Hello'
if x < 1:
    print("X is less than 1")
elif my_var == "Hello":
    print("My var was hello")
else:
    print("Neither condition were matched")'''
######################################################################3

'''x = float(input('Enter a number: '))
my_var = 'Tati'
if x < 1:
    print("X is less than 1")
elif my_var == "Alex":
    print("My var was hello")
else:
    # We should not do anything in this case
    pass  # Pass doesn't do anything, a so called no-op.'''

######################  FUNCTION#############3

'''def greet_someone_somewhere_default_sweden(name, location="Sweden"):
    return f"Hello {name}, nice to see you in {location}!"
greet_someone_somewhere_default_sweden("Alex")'''

some_num = 0
while some_num < 10:
    print("Running")
    print(some_num)
    some_num = some_num + 1




