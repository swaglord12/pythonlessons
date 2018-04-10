# lecture 38 list comprehensions
mystring = 'hello'
mylist = []

# append the string into a list using
# a for loop
for letter in mystring:
    mylist.append(letter)

print(mylist)

# more efficient way of doing this
# not code efficient just space / code
# using list comprehension NOT for loop like above.
mylist1 = [letter for letter in mystring]
print(mylist1)

mylist2 = [x for x in 'word']
# basically its element for element
# in an iterable object
print(mylist2)

mylist3 = [num for num in range(0,11)]
print(mylist3)

# will only print nums that are even
mylist4= [x for x in range(0,11) if x%2 == 0]
print(mylist4)

