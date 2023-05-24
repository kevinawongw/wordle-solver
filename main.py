"""
    main.py
"""
import argparse
import random
from utils import check_string,insist_correct,read_words
from solver import wordle_solver

def get_args():
    """
        Custom args
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--init',
                        required = False,
                        default = '',
                        action = 'store',
                        help='initial guess for non randomized start')
    args = parser.parse_args()
    return args

def main():

    """
        Main
    """
    args = get_args()
    init_guess = args.init
    words = list(read_words("words.txt"))
    if not check_string(init_guess):
        print("Initial guess was not a valid option. Selecting random starting word.")
        guess = random.choice(words)
    else:
        guess = init_guess
    found_letters = []
    count = 1
    print("\nf'Initial Guess: {guess}")

    print("\n-   _ indicating incorrect\n-   * indicating correct letter, incorrect spot\n")
    print("-   Any letter indicating correct value/spot\n(ie. _ _ _ * K)\n\n")
    result = input("Input Result:")
    result = insist_correct(result)

    init_pool = words

    while "_" in result or "*" in result:
        ending_pool,found_letters = wordle_solver(guess,result,init_pool,found_letters)
        init_pool = ending_pool
        print(ending_pool)
        if len(ending_pool) == 1:
            guess=ending_pool[0]
        elif len(ending_pool) == 0:
            return "no more guesses.."
        else:
            guess = random.choice(init_pool)
        print("\nf'Next Guess: {guess}")
        result = input("Input Result:")
        result = insist_correct(result)

        count+=1
        if count==6:
            print("sorry:(")
            return


    print("CONGRATS :)")
    return
if __name__ == '__main__':
    main()
