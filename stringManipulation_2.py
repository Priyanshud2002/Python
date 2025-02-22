print("Hello world!".startswith("hello")) #true
print("Hello world!".endswith("world!"))  #true
print(', '.join(['cats', 'rats', 'bats']))  #joins the list with ','
print('ABC '.join(['my', 'name', 'is', 'simon'])) #joins it with ABC
print("My name is Simon".split()) #splits every word in the string
print('MyABCnameABCisABCSimon'.split('ABC')) #splits ABC from the string
print('My name is Simon'.split('m')) #splits every m from the string
print('Hello'.rjust(10)) #5 spaces added to the left
print("hello".ljust(10))  #5spaces added to the right
print("hello".center(10))  #centered with spaces
print("hello".rjust(20, "*")) #prints '*' instead of spaces from left side
print('Hello'.ljust(20, '*')) #prints '*' instead of spaces from right side
print('Hello'.center(20, '*')) #prints '*' from left and right both till center
