import random
def guessGame():
    secretAnime = ["Jobless Reincarnate", "Naruto", "Bleach", "JJK", "Bleach", "Demon Slayer"]
    guess = ""
    realGuess=random.choice(secretAnime)
    guessCount = 0

    while guess!=realGuess and guessCount!=3 :
        if guessCount !=3 :
            guess=input("Enter An Anime :" + " ")
        guessCount=guessCount+1

    if guessCount ==3 and guess!=secretAnime:
        print("Sorry You Lost The Anime Was "+ realGuess )
        play=input(" Wanna Play Again : "+" ")
        if (play=="Yes" or play=="yes" or play=="YES"):
            guessGame()
        else:
            print("OK Have A Nice Day !!")
    else:
        play = input("WOOHOO !! You Won Wanna Play Again : " + " ")
        if (play == "Yes" or play == "yes" or play == "YES"):
            guessGame()
        else:
            print("OK Have A Nice Day !!")

guessGame()
