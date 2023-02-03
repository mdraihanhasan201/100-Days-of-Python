from guess import logo
from random import randint
print(logo)

EASY_LAVEL_TURN=10
HARD_LEVEL_TURN=5


def check_answer(guess,answer,turns):
    if guess>answer:
        print("too high")
        return turns - 1
    elif guess<answer:
        print("too low")
        return turns - 1

    else:
        print(f"you got it , your ans is {answer}")


def set_difficulity():
    level=input(" chose a difficulity , type 'easy ' or 'hard':\n")
    if level=="easy":
        return EASY_LAVEL_TURN
    else:
        return HARD_LEVEL_TURN


def game():
    print("i'am thinking of number between i and 100.")


    answer=randint(1,100)
    # print(f"the correct answer is {answer}")

    turns=set_difficulity()



    guess=0
    while guess != answer:
        print(f"you have {turns}  attempts remaining to guess the number ")

        guess=int(input("input a guess number"))
        turns = check_answer(guess,answer,turns)
        if turns==0:
         print("you ran out of guesses, you lose!")
         return
        if guess != answer:
            print("guess again")



game()








