#!/usr/bin/env python3
import random

# wordlist fixing
f = open('english.txt','r').read()
wordlist = []

for x in f.split('\n'):
    wordlist.append(x)

phrase = ''

frstRandom = random.choice(wordlist)
phrase += frstRandom

numberLoop = 0

while True:
    if numberLoop == 15:
        print(numberLoop)
        print(phrase)
        break
    randomChoice = random.choice(wordlist)
    firstCharacterOfLastWord = phrase.split(' ')[-1][0]
    if firstCharacterOfLastWord == randomChoice[0]:
        pass
    else:
        phrase += ' ' + randomChoice
        numberLoop += 1
