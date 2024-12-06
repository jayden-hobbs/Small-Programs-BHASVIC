from random import randint

def dice_score(dice1, dice2, dice3):
    if dice1==dice2 and dice2==dice3:
        score = dice1+dice2+dice3
    else:
        if dice1==dice2:
            score = dice1+dice2-dice3
        elif dice2==dice3:
            score = dice2+dice3-dice1
        else:
            score = 0
    return score
dice1=random.randint(1,6)
dice2=random.randint(1,6)
dice3=random.randint(1,6)

print(dice1)
print(dice2)
print(dice3)

print(dice_score(dice1, dice2, dice3))