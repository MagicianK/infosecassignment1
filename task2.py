import string

alphabet = list(string.ascii_lowercase)
r_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

# Format for our program input is english_word-russian_word
word = input("Input words in format english_word-russian_word: ")
k = int(input("Key number for Caesar: "))
print(alphabet)
print(r_alphabet)

isrussian = False

nword = ""
for letter in word:
    letter = letter.lower()
    if letter == '-':
        isrussian = True
    if isrussian and not letter in [' ', '-']: 
        nword += r_alphabet[(r_alphabet.index(letter) + k) % 33]
    elif not letter in [' ', '-']:
        nword += alphabet[(alphabet.index(letter) + k) % 26]
    else:
        nword += letter

print(word)
print(nword)




