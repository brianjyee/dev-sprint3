# This is where the answers to Chapter 9 questions for the BSS Dev RampUp go
# Name: Brian Yee

def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

def uses_only(word, letters):
    for letter in word:
        if letter not in letters:
            return False
    return True

allowed = raw_input("Enter some letters:")
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if uses_only(word, allowed):
        print word