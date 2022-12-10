import string
import random

word = input("Input your word: ")
alphabet = list(string.ascii_lowercase)
alphabet.remove('j')
ralphabet = alphabet
random.shuffle(ralphabet)
nword = ""

for letter in word:
    if letter != " ":
        if letter.lower() == "j":
            letter = "i"
        index = ralphabet.index(letter.lower())
        nword += ralphabet[(index + 5) % 25]
    else:
        nword += " "

dword = ""
for letter in nword:
    if letter != " ":
        index = ralphabet.index(letter)
        dword += ralphabet[(index - 5) % 25]
    else:
        dword += " "


print("Random alphabet:")
for i in range(25):
    print(alphabet[i], end=" ")
    if (i + 1) % 5 == 0:
        print()
print("Word: ")
print(word)
print()
print("New word: ")
print(nword)

print()
print("decrypted: ")
print(dword)






