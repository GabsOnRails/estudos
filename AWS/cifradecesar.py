"""
Código para criar uma criptografia básica utilizado no módulo de Python da AWS re/start. Futuramente irei
modificar algumas coisas.
PS: A criptografia só funciona para letras, números não devem ser utilizados.
"""


def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt


'''
a função getMessage irá registrar a mensagem que o usuário quer criptografar.
'''


def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet


'''
a função getDoubleAlphabet tem o intuito de duplicar o alfabeto para a criptografia.
'''


def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return shiftAmount


'''
A função getCipherKey irá registrar o número da chave de codificação para a criptografia.
'''


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


'''
A função de criptografia utilizar as funções anteriores, mas funciona atráves do input do usuário. A frase
escrita é colocada em letras maiusculas (upper) e após isso a chave de codificação (cipherkey) é usada. Exemplo, digitamos a palavra A e a cypherkey 2, a função irá criptografar somando o indice de A + 2 e buscar no alfabeto o que é correspondente, no caso a letra C. Esse processo é realizado em todas as letras do input inicial e assim a mensagem é criptografada.
'''


def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)


'''
Para essa criptografia simples, podemos  desfazer a criptografia mudando cada letra de volta. Logo, em vez de adicionar a chave de cifra, iremos  subtrair a chave. Para evitar reescrever a maior parte da lógica, uma chave de cifra negativa será usada.
'''


def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')


runCaesarCipherProgram()
