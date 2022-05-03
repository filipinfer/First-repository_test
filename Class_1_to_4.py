# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


'''def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''

'''num_list = []
our_tup = (1, 3, 7, None, 'abc')
for element in our_tup:
    if isinstance(element, str):
        num_list.append(element)

print(our_tup)
print(num_list)'''

##num_list = [element for element in our_tup if isinstance(element, int)]
##print(num_list)

'''my_dictionary = {'name': 'Ada Lovelace', 'age': '20', 'born_year': '1987'}
dict_name = { key: value for key, value in my_dictionary.items() if key == "age" }
print(dict_name)'''

'''my_dictionary = {'name': 'Ada Lovelace', 'age': '20', 'born_year': '1987', 'city': 'New York'}
extract_keys = {"name", "born_year", "city"}
dict_name = {
    key: value
    for key, value in my_dictionary.items()
    if key in extract_keys
}
print(dict_name)'''
'''
other_empty_var = []
##other_empty_var is None
if other_empty_var is None:
    print("We didn't get anything back")
elif other_empty_var is not None:
    print("The varible has some kind of value")
'''

'''from typing import Optional

# <= 3.9 Syntax
def maybe_none(arg: int) -> Optional[int]:
    if arg > 1:
        return arg
print(maybe_none(-98))'''

'''from typing import Optional

# <= 3.9 Syntax
def maybe_none(arg: int) -> int | None:
    if arg > 1:
        return arg
print(maybe_none(0))'''

'''password = "abc12309"
if len(password) < 8:
    print(f"Your password is {len(password)} characters long, min is 8 characters")
else:
    print("Password accepted")'''

'''def greet_someone(name, location):
    return f"Hello {name}, welcome to {location}"

print(greet_someone('Maria', 'Rome'))'''
'''def greet_someone(name, location):
    return f"Hello {name}, welcome to {location}"
greetings = (
    ("Alex", "Gothenburg"),### linha 0
    ("Åsa", "Linköping"),## linha 1 
)
print(greet_someone(greetings[1][0], greetings[0][1]))

## greeting: 0 de cima, primeiro greeting dos 2
# greeting: 1 de baixo

# gotemburgo
## linkoping'''

# def greet_someone(name, location):
# return f"Hello {name}, welcome to {location}"
'''greetings = (
    ("Alex", "Gothenburg"),
    ("Åsa", "Linköping"),
)
greet_someone(greetings[0][0], greetings[0][1])
for greeting in greetings:
    print(greet_someone(*greeting))'''

##greet_someone('Leila','Suica')
# print(greet_someone('Leila','Suica'))


'''def greet_someone(name, location, age):
    return f"Hello {name}, welcome to {location}"
greeting_dict = {
     "name": "Hans-Göran",
     "location": "Malmö",
     "age": "20"

}
print(greet_someone(**greeting_dict))'''
##failing test
'''def greet_someone(name, location):
    return f"Hello {name}, welcome to {location}"
assert greet_someone("Alex", "Gothenburg") == "Kalle Anka"
print("Will it reach this code?")'''

# Passing test
'''def greet_someone(name, location):
    return f"Hello {name}, welcome to {location}"
assert greet_someone("Alex", "Gothenburg") == "Hello Alex, welcome to Gothenburg"
assert "Hello Åsa, welcome to Linköping" == greet_someone("Åsa", "Linköping")

print("Will it reach this code?")'''

##import pytest

'''def greet_someone(name, location):
    return f"Hello {name}, welcome to {location}"

def test_greet_someone():
    "A function to test the greet_someone() function"
    assert greet_someone("Alex", "Gothenburg") == "Hello Alex, welcome to Gothenburg"
    assert "Hello Åsa, welcome to Linköping" == greet_someone("Åsa", "Linköping")

test_greet_someone()'''

# A basic class
# A basic class
'''class Student:
    # Initializer, runs when calling Student() to create new obj
    # Self is injected automatically
    def __init__(self, name, age, gender, surname):
        # Setup our values
        self.name = name
        self.age = age
        self.gender = gender
        self.surname = surname
    # Greeter method
    def greet(self):
        return f"Hello {self.name} {self.surname}"
## created instance for the object
Fernanda = Student('Fernanda', 18, 'female', 'Filippin')
print(Fernanda.surname, Fernanda.gender)
print(Fernanda.greet())'''

# Exceptions, try-except-finally

'''cleanup_error = print
try:
  # Will always error
  assert False, "Our error message"
  never_runs()  # This code won't be raised
except AssertionError as err:
  # Will only run on errors
  print("Caught error")
  print(err)
  # These two lines are the same
  raise
  # raise err
finally:
  # Will always run
  cleanup_error("Do our cleaning")

print("Errornous code completed")'''

'''def is_positive(x):
  if x < 0:
    raise ValueError("X must be positive")
  return x


print(is_positive(-1))'''

'''def is_positive(x):
    try:
        is_positive(-1)
    except ValueError as my_err:
        print(my_err)
        # Value error is caught, and ignored in this case
        pass

print("This should be printed")'''

user_age = None

'''def is_positive(x):
    if x < 0:
        raise ValueError("X must be positive")
    return x

#print(is_positive(1))

# Ask for the age, until it's no longer None
while user_age is None:
    try:
        user_age = is_positive(int(input('Digite a idade: ')))
    except ValueError as err:
        print(err)
        print("Please try again")


if user_age == 0:
    print("Congratulations on being a newborn!")
else:
    print(f"You are {user_age} years old!")'''

# Prints out 3,5,7
#for x in range(3, 8, 2):
 #   print(x)


'''count = 0
while True:
    print(count)
    count += 1
    if count >= 9:
        break'''
'''for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)'''

# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

'''x = 0
while(x < 5):
    print(x)
    x +=1
else:
    print("count value reached %d" %(x))
'''

# Prints out 1,2,3,4    perguntar alberto
'''for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")'''



'''Loop through and print out all even numbers from the numbers list in the same order they are received. 
Don't print any numbers that come after 237 in the sequence.'''
'''numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
for number in numbers:
    if number % 2 == 0:
        print(number)
    if number == 237:
        break
print('Numbers after 237 in the list shouldnt be displayed')'''


##############################################


# your code goes here
'''numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]
for number in numbers:
    if number == 237:
        break

    if number % 2 == 1:
        continue

    print(number)
'''


'''sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
      if word != "the":
          word_lengths.append(len(word))
print(words)
print(word_lengths)'''

#Using a list comprehension, create a new list called "newlist" out of the list "numbers", which contains only
#the positive numbers from the list, as integers.

'''numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = []
for number in numbers:
    if number >= 0:
        newlist.append(int(number))
print(newlist)'''

### dictionaries

'''phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))'''

## Removing a value
'''phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
del phonebook["John"]
print(phonebook)'''

'''phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
phonebook["Jake"] = 938273443
del phonebook["Jill"]
#print(phonebook)
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")'''

#### Sets ##########
#In the exercise below, use the given lists to print out a set containing all
# the participants from event A which did not attend event B.

'''a = set (["Jake", "John", "Eric"])
b = set (["John", "Jill"])

print((a.difference(b)))    #'The participants which didnt attend the event B are: ')
#print(b.difference(a))
'''

##### FUNCTIONS
#
'''def my_function():
    print("Hello From My Function!")
my_function()'''


'''def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))
my_function_with_args('Fernanda','good luck')'''


'''def sum_two_numbers(a, b):
    return a + b
print(sum_two_numbers(1,2))'''

'''def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse",
            "Allowing programmers to share and connect code together"]
print(list_benefits())

def build_sentence(benefit):
    return f'is a {benefit} of functions!'
print(build_sentence('benefit'))

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()'''

import pytest
'''def sum_of_two_numbers(x,y):
    return x + y
print(sum_of_two_numbers(1,2))


def test_sum_of_two_numbers():
    assert sum_of_two_numbers(1,2) == 3

test_sum_of_two_numbers()'''

'''def welcome(name,location):
    print('Hi', name, 'welcome to', location)
welcome('Fernanda','USA')'''


'''def add(x,y):
    return x + y
if add(2,4) == 9:
        print('That is what we expected')
result = add(4,7)
print(f'A soma de X e y é: {result}')'''

'''def optional_greeter(name):
    if name.startswith('X'):
        # We don't greet people with weird names :p
        pass
    else:
        print('Hi there, ', name)
print(optional_greeter('Xander'))'''


'''def welcome(name='learner', location='this tutorial'):
    print("Hi", name, "welcome to", location)

welcome()'''

'''try:
    print(2/0)
except ZeroDivisionError:
    print("You can't divide by zero!")'''




















