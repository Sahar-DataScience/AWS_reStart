"""
Using Functions to Implement a Caesar Cipher
"""
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
    
#="ABC"
#print(getDoubleAlphabet(alphabet))

def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt
    
def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage
    
def decryptMessage(message, cipherKey, alphabet):
        
    decryptKey = -1 * int(cipherKey)
        
    return encryptMessage(message, decryptKey, alphabet)

alphabet = "ABCDEFJHIGKLMNOPQRSTUVWXYZ"
alphabet = getDoubleAlphabet(alphabet)
message = getMessage()
cipherKey = getCipherKey()
encrypted = encryptMessage(message, cipherKey, alphabet)
print("the encrypted msg:", encrypted)
print("the decrypted msg:",decryptMessage(encrypted, cipherKey, alphabet))