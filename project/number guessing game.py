from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#function to check users guess against actual answer

def check_answer(guess,answer,turns):
    
    if (guess>answer):
        print("High Number")
        return turns - 1
    elif guess < answer:
        print("Low Number")
        return turns - 1
    else:
        print(f"you got it ! the answer was {answer}")


def set_difficulty():
    level = input("choose a difficulty. type 'easy' or 'hard':")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
def game():
    print("welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)

    turns = set_difficulty()
    guess= 0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the nmber:")

        guess = int(input("make a guess:"))
        turns = check_answer(guess, answer,turns)
        if turns == 0:
            print("you've run out of guessess, you lose.")
            return
        elif guess != answer:
            print("guess again")

game()




