import random
from words import *
from sys import exit
from PyDictionary import PyDictionary

dictionary=PyDictionary()

def main():
    game_instruction()
    check_answer(secret_word)

def game_instruction():
    print('\n### WORDLE ###')
    print("""\nWordle, the online word game is very easy to play and has very simple rules that one can go through.
1. The player has to guess the Wordle in six attempts or less.
2. Every word, which is entered should be in the word list.
3. If the letter is correct, the terminal will return the letter in the correct place.
4. If the letter is correct but placed wrong then it would return '🟧'
5. An incorrect letter return '_'
6. Letters can be used more than one time \n""")


# get random word
secret_word = random.choice(WORDS)



# function to check the format of the guess word
def check_guess():
    while True:
        user_guess = input('Guess: \n').lower()
        # check formant of guess:
        if len(user_guess) != 5:
            print('Only 5 letter word is valid...')
        elif user_guess not in WORDS:
            print('Not a valid word...')
        else:
            return user_guess


def check_answer(answer):
    attempts = 0
    while attempts < 6:
        # add clue for fun
        if attempts == 5 :
            print('Here is a clue for you:')
            print (dictionary.synonym(answer))
        guess = check_guess()
        progress = ''
        # iterate over guess and compare to secret_word
        for i in range(0,5):
            if guess[i] == answer[i]:
                progress += guess[i]
            elif guess[i] in answer:
                progress += '🟧'
            else:
                progress += '_'

        print(progress)
        attempts +=1

    if progress == answer:
        exit(f"Well done! you did it in {attempts} attempts")

    print('Oops, better luck next time :(')
    print(f" The answer is: {answer}")



if __name__ == "__main__":
    main()