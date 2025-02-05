print('Please enter your name')
name = input()  # get the name

print('Enter Your Age')
age = int(input())  # get age and convert into integer

# checking conditions
if name == 'Priyanshu' and age == 22:
    print('Hi ' + name)
elif age < 12:
    print('Hey Kiddo')
elif age > 50:
    print('Hey Old Man')
