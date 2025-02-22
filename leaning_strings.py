print("Hello" in "Hello World") #output would be true because it is true
print("hello" in "hello")  #output would be true
print("HELLO" in "Hello World")  #False (case sensitive)
print('' in 'spam') #True (empty string is always "inside' another string

print("cats" not in "cats and dogs") #output would be false because cats exist
print("lion" not in "cats and dogs") #true because lion is not in the string

text = "Hello world!"

text_upper = text.upper() #converts texts to uppercase
print(text_upper)

text_lower = text.lower() #converts text to lowercase
print(text_lower)

print("HELLO".isupper()) #output would be True(string is in uppercase)
print("hello".islower()) #true (string is in lowercase)
print("Hello".isupper()) #false (only 'h' is in uppercase)
print('hello123'.islower()) #true (numbers are ignored)
print("12345".islower()) #false (NO letters )

print("how are you?")
feeling = input()

if feeling.lower() == 'great':
    print("i feel great too.")
else:
    print("I hope the rest of your day is good")

print("hello".isalpha()) #true(contains only alphabtes)
print("hello123".isalnum()) #true(contains letters and numbers only)
print("123".isdecimal()) #true(contains only numbers)
print(" ".isspace()) #true(contains only spaces)
print("This Is Title Case".istitle()) #true(first letter is uppercase)
print("hello123".isaplha()) #false(contains numbers)
print("this is not title case".istitle()) #false(first letter is not upper case)



    
