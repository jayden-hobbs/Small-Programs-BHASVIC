a=int(input('Enter a number: '))

def fizzbuzz(a):

    if a % 3 == 0:

        return ('Fizz')

    elif a % 5 == 0:

        return ( 'Buzz' )

    elif a % 15 == 0:

        return ('Fizzbuzz')

    else:

        return a

print(fizzbuzz(a))
fizzbuzz(a)