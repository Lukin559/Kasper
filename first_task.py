import re
with open('task1.txt') as file:
    text = file.read()

alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
ALPHABET = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
stext = text.split('?')
sentences = []

for sentence in stext:
    if sentence.find('.') != -1:
        sentences.append(sentence.split('.')[-1])
    else:
        sentences.append(sentence)
print(sentences)

for sentence in sentences:
    for pos in range(len(alphabet)):
        print(pos, end=' ')
        for letter in sentence:
            if letter in alphabet:
                print(alphabet[(alphabet.index(letter) - pos) % len(alphabet)], end='')
            elif letter in ALPHABET:
                print(ALPHABET[(ALPHABET.index(letter) - pos) % len(ALPHABET)], end='')
            else:
                print(letter, end='')
        print('')