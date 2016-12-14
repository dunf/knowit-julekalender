#!/usr/bin/python

def decToRoman(number):         # Returns the roman number in decimal
    return ['0', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII'][int(number)]

def letterToDecimal(letter):    # Returns a letters position in the alphabet
    return ord(letter) - 64 if ord(letter) - 96 < 0 else ord(letter) - 96

if __name__ == '__main__':
    message = "Your message was received with gratitude! We do not know about you, but Christmas is definitely our favourite holiday. The tree, the lights, all the presents to unwrap. Could there be anything more magical than that?! We wish you a happy holiday and a happy new year!"
    ciphertext = []
    for char in message[::-1]:
        if char not in (' ', ',', '.', '!', '?'):
            value = letterToDecimal(char)
            p = value / 2 if value % 2 == 0 else value / 2 + 1
            ciphertext.insert(0, decToRoman(p))
            ciphertext.append(decToRoman(int(value / 2)))
    print(', '.join(ciphertext))


