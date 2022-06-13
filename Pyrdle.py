import random

ATTEMPTS = 5
attempt_number = 5
word_length = 5
is_valid = False
reset = False
guess_dict = {
    "0": "last",
    "1": "fifth",
    "2": "forth",
    "3": "third",
    "4": "seccond",
    "5": "first"
}

def random_word():
    pyrdle = random.choice(open("wordlib.txt").readlines())
    pyrdle = pyrdle.replace("\n","")
    print("Ssssshh.. The random word is: " + pyrdle + " (this is for debug purposes)")
    print("All guesses must be " + str(word_length) + " letter words")
    return pyrdle

def take_user_guess():
    while is_valid == False:
        guess = input("What is your " + str(guess_tracker()) + " guess: ")
        guess = guess.upper()
        if len(guess) != word_length:
            print("Sorry, your answer must be a " + str(word_length) + " letter word.")
            continue
        if not guess.isalpha():
            print("Sorry, your answer must only contain letters.") 
            continue
        if check_word(guess) == False:
            print("Sorry, your answer must be a real word.")
            continue
        event_correct_guess()
        return guess

def guess_tracker():
    return guess_dict[str(attempt_number)]

def event_correct_guess():
    global attempt_number
    if attempt_number <= 0:
        event_loss()
    else:
        attempt_number = attempt_number - 1

def check_word(guess):
    with open('wordlib.txt') as f:
        if guess not in f.read():
            return False

def eval_guess(guess, pyrdle):
    result = ""
    if guess != pyrdle:
        for i in range(word_length):
            if guess[i] == pyrdle[i]:
                result += "g"
            elif guess[i] in pyrdle:
                result += "y"
            elif guess[i] not in pyrdle:
                result += "x"
        print(result)
        return False
    else:
        return True

def event_win():
    print("Congrats")

def event_loss():
    print("Sorry, you lost.")
    event_replay()

def event_replay():
    global attempt_number
    playAgain = input("Do you want to play again? (Yes/No)")
    if playAgain.upper() == "YES":
        attempt_number = ATTEMPTS
        main()
    else: exit()

def main():
    global reset
    win = False
    pyrdle = random_word()
    while win == False:
        guess = take_user_guess()
        win = eval_guess(guess, pyrdle)
    event_win()
    event_replay()

if __name__ == "__main__":
    main()