#states of water problem
#subroutine to delcare temp ranges in water
def what_state(Temp):
    if Temp >= 100:
        return "gaseous"
    elif Temp >= 1 and Temp <= 99:
        return "liquid"

#main programme
print(what_state(23))