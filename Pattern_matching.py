def isPhoneNumber(text):  # +91-9351394938
    if len(text) != 14:
        return False

    if text[0] != "+":
        return False

    for i in range(1, 3):
        if not text[i].isdecimal():
            return False

    if text[3] != "-":
        return False

    for i in range(4, 14):
        if not text[i].isdecimal():
            return False

    return True

print(isPhoneNumber("+91-9351394938"))  # ✅ True
print(isPhoneNumber("91-9351394938"))   # ❌ False (Missing "+")
print(isPhoneNumber("+9A-9351394938"))  # ❌ False (Letter in country code)
print(isPhoneNumber("+91*9351394938"))  # ❌ False (Wrong separator)
print(isPhoneNumber("+91-93513A4938"))  # ❌ False (Letter in phone number)
print(isPhoneNumber("+911-935139493"))  # ❌ False (Wrong length)

message = " Call me at +91-9351394938 tomorrow. +91-7014375623 is my old number!"

for i in range(len(message) - 14 + 1): #slicing into 14
    chunk = message[i:i+14]
    if isPhoneNumber(chunk): #check if it is a valid phone number
        print("Phone Number Found:", chunk)

print("done")
