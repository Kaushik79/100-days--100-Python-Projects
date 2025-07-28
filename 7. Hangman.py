import random
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     
''')
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = [
    "python", "adventure", "galaxy", "island", "jungle", "keyboard", "library", "mystery", "ocean",
    "puzzle", "rabbit", "shadow", "treasure", "volcano", "wizard", "anchor", "banana", "candle", "dragon",
    "emerald", "forest", "guitar", "harbor", "insect", "jacket", "kitten", "lantern", "mountain", "notebook",
    "octopus", "pirate", "quartz", "rocket", "safari", "tornado", "umbrella", "viking", "whisper", "xenon",
    "yarn", "power", "science", "castle", "desert", "engine", "flamingo", "grapefruit", "helmet", "igloo"
]
chosen_word = random.choice(words)
word= ""
for i in chosen_word:
    word+= "_"
print(f"Word to guess: {word}")
result = False
correct_letters = []
lives = 6
while not result:
    print(f"**********{lives}/6 LIVES LEFT**********")
    guess = input("Guess a letter: \n").lower()
    if guess in correct_letters:
        print(f"You already guessed the letter: {guess}")
    display = ""
    for i in chosen_word:
        if guess == i:
            display+=i
            correct_letters.append(i)
        elif i in correct_letters:
            display+=i
        else:
            display+="_"
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        if lives == 0:
            result = True
            print(f"************IT WAS {chosen_word}! YOU LOSE************")
    print(display)
    if "_" not in display:
        result = True
        print("************YOU WIN************")
    print(stages[6 - lives])