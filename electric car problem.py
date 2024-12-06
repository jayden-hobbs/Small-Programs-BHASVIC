import math
def electricty(mins_spent):
    if mins_spent <= 15:
        total = 15*0.2
        points = 22
    else:
        total = mins_spent*0.2
        points = math.floor(mins_spent*1.5)
    total += 1
    return total, points
mins_spent = int(input("How many minutes did you spend here today? "))
total, points = electricty(mins_spent)

print(f"You owe £{total:.2f}")
print(f"You gained {points} points!")




