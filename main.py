import string
import keyword

text = input("Введіть вашу змінну: ")
list1 = []
for char in string.punctuation:
    if char != "_":
        list1.append(char)
for char in text:
    if char in string.ascii_uppercase:
        print(False)
    break
if text[0].isdigit():
        print(False)
        exit()
for i in list1:
        if i in text:
            print(False)
            break
while True:
    if text.count("_") > 1:
        print(False)
        break
if text in keyword.kwlist:
        print(False)
        exit()
print(True)
