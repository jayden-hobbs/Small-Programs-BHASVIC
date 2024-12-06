import random
import time

#perform discount calculations
def advertBoard():
    discount = 0
    while discount < 60:
        discount = discount + random.randint(0, 20)
        if discount >= 60:
            discount = 60
        print(discount)
        time.sleep(0.5)

#call the function
advertBoard()
