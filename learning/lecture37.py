# lecture 37
# useful operators in python
# keywords / helpful operators

# the range function in python
mylist = [1,2,3]

# will print numbers all the way up to 10
for num in range(10):
    print(num)

# will print 0 and the way to 10
for num in range(0,10):
    print(num)

# will print 0 all the way to 10 but will print all
# the even numbers based on the 2 iterator
for num in range (0,10,2):
    print(num)

word = "swagger"
for item in enumerate(word):
    print(item)

mylist1 = [1,2,3]
mylist2 = ['a','b','c']

for item in zip(mylist1, mylist2):
    print(item)