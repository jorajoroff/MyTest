# Ceasar Chiper

import pyperclip
#Junk comment for github plays
#Another junk comment and push to github

def caesarChiper():
    LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    translated =''
    word = ''
    key = ''
   
    #print ('Do you want encrypt/decrypt/quit:(e/d/q) ')
    
    while word not in ('E', 'D', 'Q'):
        print ("Type 'e' for encrypt, 'd' for decrypt or 'q' for quit!")
        word = input().upper()
        
    if word == 'E':
        mode = 'encrypt'
        print('Enter a message to encrypt: ')
    elif word == 'D':
        mode = 'decrypt'
        print('Enter a message to decrypt: ')
    elif word == 'Q':
        print ('Goodbye!')
        return
      
    message = input()
    while not key.isdigit(): 
        print ('Enter a secret key (a number): ')
        key = input()

    #message = message.upper()
    key = int(key)%len(LETTERS)
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)

            if mode == 'encrypt':
                num = num + key
            elif mode == 'decrypt':
                num = num - key
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)
                

            translated = translated + LETTERS[num]
        else:
             translated = translated + symbol
    print (translated)
    pyperclip.copy(translated)
    
