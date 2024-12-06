# scrabble problem




def scrabble_problem(userWord):
    total = 0
    for Index in range(0, len(userWord),1):
        Alpha = userWord[Index]
        if Alpha == "e" or Alpha == "a" or Alpha == "i" or Alpha == "o" or Alpha == "n" or Alpha == "r" or Alpha == "t" or Alpha == "l" or Alpha == "s" or Alpha == "u":
            total +=1
        elif Alpha == "d" or Alpha == "g":
            total+=2
        elif Alpha == "b" or Alpha == "c" or Alpha == "m" or Alpha == "p":
            total +=3
        elif Alpha == "f" or Alpha == "h" or Alpha == "v" or Alpha == "w" or Alpha == "y":
            total+=4
        elif Alpha == "k":
            total+=5
        elif Alpha == "j" or Alpha == "x":
            total+=8
        elif Alpha == "q" or Alpha == "z":
            total+=10

    return total


userWord = input("Input your word! ")
print(scrabble_problem(userWord))