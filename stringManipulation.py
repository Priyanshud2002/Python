text1 = 'Hello, world!' #using single quotes

text2 = "Hello, world!" #using double quotes

text3 = "Hey, that's my book" #using double quotes in the string so that i can
                              #single quotes inside it (that's)


text4 = 'That\'s my book' #used a single quote inside a single quoted string
                          #with the help of \


text5 = "She said, \"hello!\"" #using a double quote inside a double quoted
                               #string using \"  \"


text6 = "hello\nWorld!"  #using \n to print world in the next line


text7 = "hello\tWorld"   #using \t to for tabular space in between hello
                          #and world

text8 = "This is a backlash: \\" #for printing a backslash using \\

text9 = r'this is Carol\'s cat' #using raw strings instead of escape characters

text10 = '''Dear principal,    
this is priyanshu here,
aset department'''              #using multiline strings(''') for printing the
                                #sentence as it is.

text11 = "Dear Alice,\nEve's cat has been arrested.\nSincerely,\nBob"
                   #doing the same thing as text 11 with \n

print(text1)
print(text2)
print(text3)
print(text4)
print(text5)
print(text6)
print(text7)
print(text8)
print(text9)
print(text10)
print(text11)

spam = "Hello world!"

print(spam[0])   # First character (H)
print(spam[4])   # Fifth character (o)
print(spam[-1])  # Last character (!)

spam = "Hello world!"

print(spam[0:5])  # First 5 characters
print(spam[:5])   # Same as above
print(spam[6:])   # Characters from index 6 to the end


