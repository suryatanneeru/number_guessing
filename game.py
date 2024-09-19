import random
import time


def welcome():
    print('''Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.''')


def difficulty():
    print('''\nPlease select the difficulty level:
1. Easy   : 10 chances
2. Medium : 5 chances
3. Hard   : 3 chances''')
    while True:
        level = int(input("\nENTER YOUR DIFFICULTY LEVEL  (1,2 or 3):"))
        if level == 1:
            return 10
        elif level == 2:
            return 5
        elif level == 3:
            return 3
        else:
            print("enter 1,2 or 3")


def get_number():
    return random.randint(1, 100)


def start_game():
    chances = difficulty()
    start_time = time.time()
    number_to_guess = get_number()
    attempts = 0

    print(f'''\nGreat! You have selected the  difficulty level with {chances} chances.
Let's start the game!''')
    while attempts < chances:
        try:
            guess = int(input("ENTER YOUR GUESS  :"))

        except ValueError:
            print("PLEASE SELECT A VALID NUMBER")

            continue

        attempts += 1

        if number_to_guess > guess:
            print('INCORRECT! THE NUMBER IS GREATER THAN', guess)

        elif number_to_guess < guess:
            print('INCORRECT! THE NUMBER IS LESSER THAN', guess)

        else:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f'Congratulations! You guessed the correct number in {attempts} attempts.')
            print(f'TIME TAKEN :{elapsed_time} seconds')
            return attempts

    print(f'\nSORRY YOU RAN OUT OF CHANCES. THE CORRECT NUMBER WAS {number_to_guess}')
    return attempts


def main():
    high_scores = {'easy': 0, 'medium': 0, 'hard': 0}
    while True:
        welcome()
        attempts = start_game()

        if attempts > high_scores['easy']:
            print('NEW HIGH SCORE FOR EASY DIFFICULTY !')
            high_scores['easy'] = attempts

        elif attempts > high_scores['medium']:
            print('NEW HIGH SCORE FOR MEDIUM DIFFICULTY !')
            high_scores['medium'] = attempts

        elif attempts > high_scores['hard']:
            print('NEW HIGH SCORE FOR HARD DIFFICULTY !')
            high_scores['hard'] = attempts

        print('\nCURRENT HIGH SCORES  :')
        print(f"EASY  :{high_scores['easy']} attempts")
        print(f"MEDIUM  :{high_scores['medium']} attempts")
        print(f"HARD  :{high_scores['hard']} attempts")

        play_again = input('''\nDO YOU WANT TO PLAY AGAIN  :
        yes or no  : ''').strip().lower()

        if play_again != 'yes':
            print('''\nTHANK YOU FOR PLAYING......!
            HAVE A GREAT DAY''')
            break

main()
