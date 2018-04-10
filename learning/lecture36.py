#lecture 36
#while loops
x = 0
#while x is less than 5
while x < 5:
    print(f"the current vale of x is : {x}")
    x = x + 1

#breaks continues and pass

x = [1,2,3]
# pass is used by programmers as a pass
# they know they want a loop there,but are not ready
# to write that code just yet.
for i in x:
    pass

mystring = "sammy"
for letter in mystring:
    if letter == 'a':
        # if the letter is a it will skip a
        # and continue going through the loop
        continue
    print(letter)


mystring = "sammy"
for letter in mystring:
    if letter == 'a':
        # if the letter is a it will completely stop the program
        break
    print(letter)

x = 0

while x < 5:
    if x ==2 :
        break
    print(x)
    x = x + 1
    