# lecture 41
# methods and python documentation
mylist = [1,2,3]
mylist.append(4)
mylist.append(5)
mylist.pop()

# lecture 42
# functions

# define function
def say_hello():
    print("hello")

# executing function
say_hello()

# define function with parameters
# if no name it will spit out "default"
def say_hello1(name='default'):
    print("hello " +name)

# executing function with name parameter given as shane
say_hello1("shane")

# save the result of your function to a variable
# first we are going to need to change "print" to "return"
# this is because printing a value and returning a value are two different
# things.
def say_hello2(name='brian'):
    return("hello " +name)

# now store the value of say hello2
# as result
result = say_hello2()

# result should be "hello brian"
print(result)

# Add function
def add(n1,n2):
    return n1 + n2

#result1 is adding 2+2
result1 = add(2,2)

print(result1)


# Find out if the word dog is in a string
def dog_check(mystring):
    'dog' in mystring.lower()

dog_check("I love Dogs")

# Pig Latin excercise
def pig_latin(word):
    first_letter = word[0]
    vowel = 'aeiou'
    #check if vowel
    if first_letter in vowel:
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word

final = pig_latin("apple")

print(final)







