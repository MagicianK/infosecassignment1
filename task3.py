import string

word = input("Input your word to cypher: ")

key = input("Input your key: ")

# non repeating word (letters won't repeat)
nrword = "".join(dict.fromkeys(key))

alphabet = list(string.ascii_lowercase)
alphabet.remove('j')

# deleting 'j' from our non repeating word (letter won't repeat)
nrword = list(nrword)
if 'j' in nrword:
    nrword[nrword.index('j')] = 'i'

for letter in nrword:
    alphabet.remove(letter)

alphabet = nrword + alphabet

# just shifting our alphabet to 5 and choosing a letter
nword = ""
for letter in word:
    if letter.lower() == "j":
        letter = "i"
    index = alphabet.index(letter.lower())
    nword += alphabet[(index + 5) % 25]

print(nword)

# Showing alphabet in square 5x5 format matrix
for i in range(25):
    print(alphabet[i], end=" ")
    if (i + 1) % 5 == 0:
        print()
