import numpy as np


# Get the solution to the puzzle
def get_solution():
    with open("solutions.txt", "r") as file:
        answers = file.read()
        words = answers.split()
    return np.random.choice(words)

# ask user for input
def ask_for_guess():
    guess = input('Enter your guess:')
    with open("valid-wordle-words.txt", 'r') as file:
        valid_list = file.read()
        valid_words = valid_list.split()
    if guess not in valid_words:
        raise ValueError("Your guess must be a valid 5 letter word")
    return guess

def compare_input_to_solution(guess, solution):
    guess_letters = ([*guess])
    solution_letters = ([*solution])
    response = [0, 0, 0, 0, 0]
    for i in range(len(guess_letters)):
        #just doing green letters for now
        if guess_letters[i] == solution_letters[i]:
            response[i] = 1
        #TODO: Handle double letters
        elif guess_letters[i] in solution_letters:
            response[i] = 0.5
    return response





def check_for_win(guess, solution):
    if guess == solution:
        return True
    else:
        return False


def main_game():
    solution = get_solution()
    Win = False
    for i in range(6):
        guess = ask_for_guess()
        #TODO: Fail gracefully if word is invalid
        response = compare_input_to_solution(guess, solution)
        print(response)
        if check_for_win(guess, solution):
            Win = True
            print("You Win!")
            break
    if Win is False:
        print("You Lose.")
    print("The Game has ended")

main_game()

