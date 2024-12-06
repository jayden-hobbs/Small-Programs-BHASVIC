def getMeal():
    ValidChoice = False
    while ValidChoice = False
        mealChoice = input(str("Please enter one of the following three meals: Breakfast (b) Lunch (l) Dinner (d): "))
    return mealChoice


def validAnswer(mealChoice):
    if mealChoice == "b" or mealChoice == "l" or mealChoice == "d":
        ValidChoice = True
    else:
        print("Invalid input.")


def actionMeal(mealChoice):
    if mealChoice == "b":
        print("Hopper 1")
    elif mealChoice == "l":
        print("Hopper 2")
    elif mealChoice == "d":
        print("Hopper 1 and Hopper 2")

getMeal()
validAnswer()
actionMeal()