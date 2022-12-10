import string

word = input("Input your word to cypher: ")

key = input("Input your key: ")

nrword = "".join(dict.fromkeys(key))

alphabet = list(string.ascii_lowercase)
alphabet.remove('j')

nrword = list(nrword)
if 'j' in nrword:
    nrword[nrword.index('j')] = 'i'

for letter in nrword:
    alphabet.remove(letter)

alphabet = nrword + alphabet

nword = ""

for letter in word:
    if letter.lower() == "j":
        letter = "i"
    index = alphabet.index(letter.lower())
    nword += alphabet[(index + 5) % 25]

print(nword)

for i in range(25):
    print(alphabet[i], end=" ")
    if (i + 1) % 5 == 0:
        print()
