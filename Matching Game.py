color = "red"
guessColor = ""
guessColorCount = 0
limit = 3
food = "beef"
guessFood = ""
guessFoodCount = 0
out_of_guess = False

while guessColor != color and not(out_of_guess):
    if guessColorCount < limit:
        guessColor = input("Enter her Favourite Color: ")
        guessColor = guessColor.lower()
        guessColorCount += 1
    else:
        out_of_guess = True
if out_of_guess:
    print(" You Lost Man ! ")
else:
    print(color.upper() + " is her favourite!")
    while guessFood != food and not(out_of_guess):
        if guessFoodCount < limit:
            guessFood = input("Enter her Favourite Food: ")
            guessFood = guessFood.lower()
            guessFoodCount += 1
        else:
            out_of_guess = True
    if out_of_guess:
        print("50 % Chance to win her")
    else:
        print(food.upper() + " is her favourite food !")
        print("It's time to meet with her !!!")



