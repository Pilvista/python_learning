secretWord = "Donkey"
guess = ""
guessCount = 0
guesslimit = 3
out_of_guesses = False


while guess != secretWord and not(out_of_guesses):
    if guessCount < guesslimit:
        guess = input("Enter Guess: ")
        guessCount += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You Lost !")
else:
    print("You Win")