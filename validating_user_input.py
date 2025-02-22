while True:
    print("Please Enter Your Age")
    age = input()

    if age.isdecimal(): #checks if age input is only number
        break
    print("Please enter a number for your age")
