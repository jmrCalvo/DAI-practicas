from random import randrange


def generateNumber():
    return randrange(100)


def getUserNumber():
    try:
        number = int(input("Enter a number: "))
        number += 0
        if number < 1 or number > 100:
            print('Must be a number between 1 and 100')
            return getUserNumber()
        return number
    except:
        print('An error ocurred, must be an Integer from 1 to 100')
        return getUserNumber()


def printLessGreatMessage(random_number, guess_number):
    if(guess_number < random_number):
        print(' The number is little')
    else:
        print(' The number is great')


def guessMessage(random_number, guess_number):
    if(random_number == guess_number):
        print('🟩 Correct, You are right')
        return True
    else:
        printLessGreatMessage(random_number, guess_number)
        return False


if __name__ == "__main__":
    random_number = generateNumber()
    # print(random_number)
    guess_number = getUserNumber()
    number_try = 1
    while(not guessMessage(random_number, guess_number) and number_try < 10):
        guess_number = getUserNumber()
        number_try += 1

    if(number_try == 10):
        print('🟥 You have tried so many times')
