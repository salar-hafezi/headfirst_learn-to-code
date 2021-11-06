import random

computer_choices = ['rock', 'paper', 'scissors']

your_choice = input('rock, paper or scissors?\n')

is_choice_valid = your_choice == 'rock' or your_choice == 'paper' or your_choice == 'scissors'

while not is_choice_valid:
    print('Invalid choice')
    your_choice = input('rock, paper or scissors?\n')
    is_choice_valid = your_choice == 'rock' or your_choice == 'paper' or your_choice == 'scissors'
computer_choice = random.choice(computer_choices)

if your_choice == computer_choice:
     print('We did the same! Let\'s play another round!')
elif (your_choice == 'rock' and computer_choice == 'scissors' ) or (your_choice == 'paper' and computer_choice == 'rock') or (your_choice == 'scissors' and computer_choice == 'paper'):
    print('You won the game!', 'Yours: ', your_choice, ', Computer: ', computer_choice)
else:
    print('You lose!', 'Yours: ', your_choice, ', Computer: ', computer_choice)

