import string
import random

word = input("Input your word: ")

# english alphabet without 'j'
alphabet = list(string.ascii_lowercase)
alphabet.remove('j')

# randomized/shuffled alphabet
ralphabet = alphabet
random.shuffle(ralphabet)

nword = "" # new encrypted text
for letter in word:
    if letter != " ":
        if letter.lower() == "j":
            letter = "i"
        # we shift by 5 because it's a letter under current letter
        index = ralphabet.index(letter.lower())
        nword += ralphabet[(index + 5) % 25]
    else:
        nword += " "

# decrypting part (reversing previous code snippet)
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






