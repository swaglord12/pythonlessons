#lecture 35
#this lecture discusses for loops in python

mylist = [1,2,3,4,5,6,7,8,9,10]

for num in mylist:
    print(num)

for num in mylist:
    print("hello")

for num in mylist:
    #check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f"odd number {num}")
list_sum = 0
for num in mylist:
    list_sum = list_sum + num
print(list_sum)

mystring = "hi im shane"

for letter in mystring:
    print(letter)

tup = (1,2,3)
for item in tup:
    print("cool")

mylist[1] = "Billy"
print(mylist)