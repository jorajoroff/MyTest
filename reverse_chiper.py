# Reverse Cipher 
def reverseChiper():
    print ('Type a message to be encripted: ') 
    message = input ()
    encripted =''

    i = len(message) - 1
    while i >=0:
        encripted = encripted + message[i]
        i -= 1

    print('Encripted message:\n' + encripted)
 
