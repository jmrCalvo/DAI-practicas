import sys
FILENAME_INPUT = "number.txt"
FILENAME_OUTPUT = "fibonacci.txt"


def fib(n):
    index = 0
    a, b = 0, 1
    while index <= n:
        if(index == n):
            print(a, end=' ')
            return 0
        else:
            a, b = b, a+b
            index += 1


def readFile():
    try:
        f = open(FILENAME_INPUT, "r")
        number = int(f.readline())
        number += 0
        return number
    except:
        return False


if __name__ == "__main__":
    f_fibonnaci = open(FILENAME_OUTPUT, 'w')
    sys.stdout = f_fibonnaci

    number = readFile()
    if(number == False and isinstance(number, bool)):
        print(
            'Not possible to read file, the file must be a number in the first line')
    else:
        if(number < 0):
            print(
                'Not negative numbers allowed')
        else:
            fib(number)
