import random
print('''
                 ,--"""--,
               .'_       _'.
        .-"-._/ / \     / \ \_.-"-.
       /.-,  /  \(o_/ \_o)/  \  ,-.\
       |   >/     _/   \_     \<   |
       \  ` |  .`( '-.-' )'.  | `  /
        '--'|  |  '-. .-'  |  |'--'
            |  | .'. | .'. |  |
            \   \___.'.___/   /
             '.  )\/-.-\/(  .'
               \/'./\_/\.'\/
                |  `"`"`  |
                |         |
                \         /
                 '._____.'
    ''')
Name = input("Enter your name: ")
print(f"{Name}, Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

roles=["scientist","explorer","solider"]
r=random.choice(roles)
print("You are the " + r + ".")
choice1 = input("You have reached a crossroad, which way would you choose? type l for left and r for right: ")
if choice1 == "l":
    print("You have entered a forest\n You found a wounded aggressive bear")
    if r == "solider":
        choice2 = input("Type 1 to fight, Type 2 to help, Type 3 to run")
        if choice2 == "1":
            print("You defeated the bear💪\n.........................\nYou found a beautiful women lying down and asking for help")
            choice3 = input("Type 1 to help, Type 2 to run")
            if choice3 == "2":
                print("She was one of the bandits.... You escaped safely👍...\n.........................\nYou found a box full of two digit numbers... you randomly picked one number...\n....\n...\n..")
                num = random.randint(10,99)
                print(f"You picked {num}\n ......\nYou reached the temple, at the gate you found 3 guards💂‍♂️\n they will let you in if your number can be divided among them equally")
                if(num%3 == 0):
                    print("You reached the treasure chest💎")
                else:
                    print("☠︎︎ You were killed by guards ☠︎︎")
            else:
                print("You were tricked, she was one of the bandits\n☠︎︎ You were killed by the Bandits ☠︎︎")
        else:
            print("☠︎︎ You were killed by the bear ☠︎︎")
    elif r == "explorer":
        choice2 = input("Type 1 to fight, Type 2 to help, Type 3 to run")
        if choice2 == "3":
            print(
                "You escaped safely🏃\n.........................\nYou found a beautiful women lying down and asking for help")
            choice3 = input("Type 1 to help, Type 2 to run")
            if choice3 == "2":
                print(
                    "She was one of the bandits.... You escaped safely👍...\n.........................\nYou found a box full of two digit numbers... you randomly picked one number...\n....\n...\n..")
                num = random.randint(10, 99)
                print(
                    f"You picked {num}\n ......\nYou reached the temple, at the gate you found 3 guards💂‍♂️\n they will let you in if your number can be divided among them equally")
                if (num % 3 == 0):
                    print("You reached the treasure chest💎")
                else:
                    print("☠︎︎ You were killed by guards ☠︎︎")
            else:
                print("You were tricked, she was one of the bandits\n☠︎︎ You were killed by the Bandits ☠︎︎")
        else:
            print("☠︎︎ You were killed by the bear ☠︎︎")
    elif r == "scientist":
        choice2 = input("Type 1 to fight, Type 2 to help, Type 3 to run")
        if choice2 == "2":
            print(
                "You healed the bear❤️‍🩹\nA loving lick from the bear 💖\n.........................\nYou found a beautiful women lying down and asking for help")
            choice3 = input("Type 1 to help, Type 2 to run")
            if choice3 == "2":
                print(
                    "She was one of the bandits.... You escaped safely👍...\n.........................\nYou found a box full of two digit numbers... you randomly picked one number...\n....\n...\n..")
                num = random.randint(10, 99)
                print(
                    f"You picked {num}\n ......\nYou reached the temple, at the gate you found 3 guards💂‍♂️\n they will let you in if your number can be divided among them equally")
                if (num % 3 == 0):
                    print("You reached the treasure chest💎")
                else:
                    print("☠︎︎ You were killed by guards ☠︎︎")
            else:
                print("You were tricked, she was one of the bandits\n☠︎︎ You were killed by the Bandits ☠︎︎")
        else:
            print("☠︎︎ You were killed by the bear ☠︎︎")
elif choice1 == "r":
    print()

else:
    print("Invalid input. Please try again.")





