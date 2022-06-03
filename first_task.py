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
print(len(stext))
print(stext)


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
keys = [17, 8, 12, 4, 7, 7, 9, 13, 20]

answer = ''

def shifr(text, key):
    global answer
    for letter in text:
        if letter in alphabet:
            answer += alphabet[(alphabet.index(letter) - key) % len(alphabet)]
        elif letter in ALPHABET:
            answer += ALPHABET[(ALPHABET.index(letter) - key) % len(ALPHABET)]
        else:
            answer += letter


for i in range(len(stext)):
    if i == 0 or i == 1:
        shifr(stext[i], keys[0])
    else:
        shifr(stext[i], keys[i-1])
# вопросительные предложения заменить вручную и все
print(answer)
