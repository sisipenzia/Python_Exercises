import random


def guessing_game():
    while True:
        randNum = random.randint(0,100)
        print("===================================================")
        print(randNum)
        guessNum = int(input("Guess the random number: "))
        if(guessNum > randNum):
            print("Too High")
        elif(guessNum < randNum):
            print("Too Low")
        elif(guessNum == randNum):
            print("Just Right")
            break
        
guessing_game()