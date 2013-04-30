# This is where the answers to Chapter 8 questions for the BSS Dev RampUp go
# Name: Brian Yee

def rotate_word(s, i):
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    rotated = ''
    for letter in s:
        for character in range(len(upper)):
            if letter == upper[character]:
                rotated += upper[(character+i)%26]
        for character in range(len(lower)):
            if letter == lower[character]:
                rotated += lower[(character+i)%26]
    return rotated
    