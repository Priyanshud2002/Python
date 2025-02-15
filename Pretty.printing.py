import pprint

message = "My name is Priyanshu, My name is Priyanshu"

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
