names = ["jayden", "ferren", "finley", "ewan", "lydia", "leo", "alex", "morgan", "logan", "ned", "joe", "joe", "luc", "mikhail", "oliver", "laura"]
name = input("Please enter a Students Name ").lower()
def counter(names, name):
    for Index in range(len(names)):
        if names[Index] == name:
            Word = names[Index]
            print("Name {} is {}.".format(Index, Word))

counter(names, name)
