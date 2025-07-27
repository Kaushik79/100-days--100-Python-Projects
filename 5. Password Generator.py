import string
import random
letters = list(string.ascii_lowercase)
digits = list(string.digits)
symbols = list(string.punctuation)
print("Welcome to the PyPassword Generator! ")
l = int(input("How many letters would you like in your password? \n"))
d = int(input("How many digits would you like in your password? \n"))
s = int(input("How many symbols would you like in your password? \n"))
password_type = int(input("Type '0' for easy password and type '1' for hard password.\n"))
password_list = []
if password_type == 0:         #generates the password in sequence. Letters then numbers and then symbols
    for i in range(l):
        print(random.choice(letters), end="")
    for i in range(d):
        print(random.choice(digits), end="")
    for i in range(s):
        print(random.choice(symbols), end="")
elif password_type == 1:       #generates password in random pattern and does not follow any sequence
    for i in range(l):
        password_list.append(random.choice(letters))
    for i in range(d):
        password_list.append(random.choice(digits))
    for i in range(s):
        password_list.append(random.choice(symbols))
    #for i in range(c):
    #    print(random.choice(password_list), end="")
    #You use random.choice(list) and print it. This will select random characters from the whole list,
    #possibly repeating or missing some characters, and the final password will NOT contain exactly the once-chosen characters.
    random.shuffle(password_list)
    print("Your password is: "+''.join(password_list))