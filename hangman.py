import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ['aardvark', 'baboon', 'camel']

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6


display = []

for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower().strip() 
    if guess in display:
        print(f"You've already guessed {guess}")   

    for position in range(0, len(chosen_word)):
        if guess == chosen_word[position]:
            display[position] = guess
    
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print("You lose")
            end_of_game = True
    print(display)
    print(stages[lives])
        
    if '_' not in display:
        end_of_game = True
        print("You win")
    
print(f"The chosen word is {chosen_word}")
