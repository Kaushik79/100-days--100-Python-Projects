import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    '''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    '''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)   
    '''

print("Let's play Rock Paper Scissors...")

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors."))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
else:
    print("Invalid choice. You lose...")

computer_choice = random.randint(0,2)
print(f"Computer chose : {computer_choice}")

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if choice == computer_choice:
    print("It's a Draw... Play again")
elif choice == 0:
    if computer_choice == 1:
        print("Computer wins!")
    elif computer_choice == 2:
        print("You win!")
elif choice == 1:
    if computer_choice == 2:
        print("Computer wins!")
    elif computer_choice == 0:
        print("You win!")
elif choice == 2:
    if computer_choice == 0:
        print("Computer wins!")
    elif computer_choice == 1:
        print("You win!")

print("Thank you for playing!")