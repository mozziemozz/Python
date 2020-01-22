import time
import random
import threading

Score = 0

def GenerateCode():
    Digit1 = random.randrange(0,9)
    Digit2 = random.randrange(0,9)
    Digit3 = random.randrange(0,9)
    Digit4 = random.randrange(0,9)
    #Digit5 = random.randrange(0,9)
    #Digit6 = random.randrange(0,9)
    Code = str(Digit1) + str(Digit2) + str(Digit3) + str(Digit4) #+ str(Digit5) + str(Digit6)
    return Code

def ShowCode():
    Code = GenerateCode()
    print(Code, end="")
    return Code

def EraseCode():
    print("\rEnter the code")

def GetChallange():
    Challenge = str(input(""))
    return Challenge

while Score >= 0:
    Code = ShowCode()
    threading.Timer(3.5, EraseCode).start()
    Challenge = GetChallange()
    if Challenge == Code:
        Score += 1
        HighScore = str(Score)
        print("Correct! Your current Score is: " + HighScore)

    else:
        print("Game Over! Your highscore was: " + str(Score))
        Score = 0
        if Score == 0:
            Repeat = str(input("Do you want to go again? y,n\n"))
        if Repeat == "y":
            continue
        if Repeat == "n":
            print("ok. bye.")
            break
        else:
            print("Invalid entry, exiting...")
            break









