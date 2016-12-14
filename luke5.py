#!/usr/bin/python

encryptedmsg = []
ciphertxt = []

#with open('luke5file') as file:
    #for line in file:
        #line = line.split("[")[1].split("]")[0].split(', ')
        #[encryptedmsg.append(sign) for sign in line]


encryptedmsg = ['XIII', 'VIII', 'XI', 'IX', 'VII', 'III', 'X', 'X', 'I', 'IV', 'III', 'XII', 'I', 'X', 'IX', 'III', 'II', 'III', 'V', 'XI', 'III', 'II', 'XII', 'V', 'X', 'IV', 'IV', 'IX', 'I', 'X', 'V', 'X', 'XI', 'II', 'III', 'XII', 'III', 'II', 'VIII', 'VII', 'VIII', 'X', 'VI', 'VII', 'VIII', 'XII', 'I', 'I', 'VIII', 'XI', 'X', 'XIII', 'VIII', 'XI', 'I', 'XI', 'X', 'II', 'IV', 'IX', 'V', 'X', 'X', 'VII', 'I', 'X', 'V', 'X', 'II', 'III', 'III', 'V', 'VII', 'V', 'X', 'III', 'VI', 'XIII', 'VIII', 'XI', 'IX', 'III', 'I', 'XI', 'VIII', 'XI', 'IX', 'V', 'X', 'III', 'IV', 'VIII', 'VI', 'V', 'II', 'I', 'XIII', 'X', 'IV', 'III', 'X', 'IX', 'III', 'III', 'X', 'IV', 'III', 'VI', 'V', 'IV', 'IV', 'X', 'X', 'I', 'VI', 'VI', 'X', 'IV', 'III', 'VIII', 'IX', 'III', 'X', 'III', 'VII', 'X', 'X', 'X', 'VIII', 'XI', 'VII', 'XII', 'IX', 'I', 'VIII', 'II', 'VIII', 'XI', 'VI', 'II', 'X', 'IV', 'III', 'IX', 'III', 'I', 'III', 'I', 'VII', 'XIII', 'X', 'IV', 'V', 'VII', 'IV', 'VII', 'VIII', 'IX', 'III', 'VII', 'I', 'IV', 'V', 'II', 'I', 'VI', 'X', 'IV', 'I', 'VII', 'X', 'IV', 'I', 'X', 'XII', 'III', 'XII', 'V', 'X', 'IV', 'XIII', 'VIII', 'XI', 'I', 'IV', 'I', 'VIII', 'VIII', 'XIII', 'IV', 'VIII', 'VI', 'V', 'II', 'I', 'XIII', 'I', 'VII', 'II', 'I', 'IV', 'I', 'VIII', 'VIII', 'XIII', 'VII', 'III', 'XII', 'XIII', 'III', 'I', 'IX', 'IX', '0', 'II', 'XII', 'XI', 'II', 'VII', 'XII', 'VIII', 'VIII', '0', 'IV', '0', 'II', 'VII', '0', 'XII', '0', 'II', 'IV', 'VI', 'VII', 'IV', 'XII', 'VIII', 'VIII', '0', 'IV', '0', 'X', 'VII', 'XII', 'IV', 'IX', 'IV', 'XI', 'II', 'XI', 'X', '0', 'IV', 'X', 'VII', '0', 'IV', 'X', 'VI', '0', 'I', 'IV', 'III', '0', 'VI', 'II', 'IX', 'VII', 'VI', 'III', 'VII', 'IV', 'IV', 'X', 'XII', 'VII', '0', 'II', 'I', 'II', 'IX', 'II', 'IV', 'X', 'II', 'VI', 'X', 'VII', 'I', 'VIII', '0', 'IX', 'XI', 'VII', 'X', 'VII', 'X', 'IX', 'X', 'VII', 'II', 'IX', 'II', 'IX', 'VIII', 'II', 'IV', 'X', 'VI', 'VI', '0', 'IX', 'X', 'IV', 'III', 'IV', 'VI', 'II', 'IV', 'X', 'II', 'II', 'IX', 'X', 'II', 'IV', 'X', 'XII', '0', 'II', 'IV', 'VI', 'VII', 'IV', 'II', 'X', 'IV', 'IX', 'X', 'VII', 'XI', '0', 'III', 'IX', 'X', 'VII', 'XII', 'VI', 'II', 'X', 'IV', 'VII', 'IV', 'III', 'II', 'II', 'IX', 'IV', 'IX', '0', 'VI', 'X', 'IX', 'IV', 'IX', 'IV', 'I', 'X', 'X', 'I', 'X', 'VII', 'XII', 'X', 'X', 'VII', 'I', '0', 'XI', 'VII', 'VII', 'V', 'X', 'VII', 'VII', 'VII', 'II', 'II', 'XI', 'II', 'II', 'X', 'X', 'IV', 'X', '0', 'IX', 'III', 'IV', 'X', 'IV', 'XI', 'II', 'II', 'XI', 'IV', 'II', 'I', 'II', 'IX', 'IX', '0', 'XI', 'II', 'III', '0', 'IX', 'IX', 'II', 'VI', 'IX', 'X', 'VII', 'XII']


def translate(romanNumber):
    romanNumbers = {
        'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8,
        'IX': 9, 'X': 10, 'XI': 11, 'XII': 12, 'XIII': 13, '0': 0 }
    return romanNumbers.get(romanNumber)

def check(encryptedmesg):
    while len(encryptedmsg) > 0:
        ciphertxt.append(translate(encryptedmsg.pop(0)) + translate(encryptedmsg.pop(len(encryptedmsg)-1)))
    cleartxt = [chr(num+64) for num in ciphertxt]
    print(''.join(cleartxt))

check(encryptedmsg)