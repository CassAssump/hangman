import random

stages = [r'''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
 
''', r'''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
 
''', r'''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
 
''', r'''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
 
''', r'''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========
 
''', r'''
 
  +---+
  |   |
      |
      |
      |
      |
=========
 
''']

with open('wordlist_pt.txt', 'r') as file:
    wordlist = file.read().splitlines() 

print ('')
chosen_word = random.choice(wordlist)

placeholder = ''
for position in range(len(chosen_word)):
    placeholder += '_'
print(placeholder)

life = 6
correct_letters = []
game_over = False

while not game_over:
    guess = input('Digite uma letra: ').lower()
    display = ''
    correct_guess = False

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_guess = True
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    if not correct_guess:
        life -= 1
        print(f'Errou! Vidas restantes: {life * " ❤️"}')

    print(display)
    if '_' not in display:
        game_over = True
        print('Você venceu!')
    if life == 0:
        game_over = True
        print('Você perdeu.')
        print(f'A palavra era: {chosen_word}!')

    print(stages[life])
