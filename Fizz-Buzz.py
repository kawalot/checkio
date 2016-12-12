#A word game used to the teach robots about division.

def checkio(number):
    if number % 3 == 0  and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    return str(number)
checkio(100)