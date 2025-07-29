print('''
   ___ __ _  ___  ___  __ _ _ __ 
 / __/ _` |/ _ \/ __|/ _` | '__|
| (_| (_| |  __/\__ \ (_| | |   
 \___\__,_|\___||___/\__,_|_|   
      _       _               
     (_)     | |              
  ___ _ _ __ | |__   ___ _ __ 
 / __| | '_ \| '_ \ / _ \ '__|
| (__| | |_) | | | |  __/ |   
 \___|_| .__/|_| |_|\___|_|   
       | |                    
       |_|                                    
''')
def encrypt(word, shift_amount):
    print("Here's the encoded result: ", end="")
    for char in word:
        o = ord(char)
        if o > 122 or o <97:
            print(chr(o), end='')
            continue
        o += shift_amount
        if o>122:
            o = 97 + (o-122-1)
        o = chr(o)
        print(o, end='')

def decrypt(word, shift_amount):
    print("Here's the decoded result: ", end="")
    for char in word:
        o = ord(char)
        if o > 122 or o <97:
            print(chr(o), end='')
            continue
        o -= shift_amount
        if o<97:
            o = 122 - (97-o-1)
        o = chr(o)
        print(o, end='')
a = True
while a:
    operation=input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
    word=input("Type your message: \n").lower()
    shift_amount=int(input("How many times would you like to shift your message: \n"))
    if operation=='encode':
        encrypt(word, shift_amount)
        reply=input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n")
        if reply == 'yes':
            a = True
        elif reply == 'no':
            a = False
    elif operation=='decode':
        decrypt(word, shift_amount)
        reply=input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n")
        if reply == 'yes':
            a = True
        elif reply == 'no':
            a = False