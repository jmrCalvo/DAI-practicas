import time
import re
from random import randrange


def burbuja_sort(array):
    start_time_burbuja = time.time()
    array_copy = array.copy()
    for nTimes in range(len(array_copy)-1, 0, -1):
        for i in range(nTimes):
            if array_copy[i] > array_copy[i+1]:
                temp = array_copy[i]
                array_copy[i] = array_copy[i+1]
                array_copy[i+1] = temp
    time_burbuja = time.time() - start_time_burbuja
    return [array_copy, time_burbuja]


def seleccion_sort(array):
    start_time_seleccion = time.time()
    array_copy = array.copy()
    for i in range(len(array_copy)):
        min_idx = i
        for j in range(i+1, len(array_copy)):
            if array_copy[min_idx] > array_copy[j]:
                min_idx = j
        array_copy[i], array_copy[min_idx] = array_copy[min_idx], array_copy[i]
    time_seleccion = time.time() - start_time_seleccion
    return [array_copy, time_seleccion]


def insercion_sort(array):
    start_time_sort = time.time()
    array_copy = array.copy()
    for i in range(1, len(array_copy)):
        key = array_copy[i]
        j = i-1
        while j >= 0 and key < array_copy[j]:
            array_copy[j+1] = array_copy[j]
            j -= 1
        array_copy[j+1] = key
    time_sort = time.time() - start_time_sort
    return [array_copy, time_sort]


def criba_eratostenes(n):
    primes = []
    isPrime = [1 for i in range(n)]
    isPrime[0] = isPrime[1] = 0

    for number in range(n):
        if isPrime[number]:
            primes.append(number)
            divisible = 2
            while number*divisible < n:
                isPrime[number*divisible] = 0
                divisible += 1
    return primes


def fib(n):
    index = 0
    a, b = 0, 1
    while index <= n:
        if(index == n):
            return a
        else:
            a, b = b, a+b
            index += 1


def check_bracket(brackets_str):
    open_char = "["
    close_char = "]"
    bracket_arr = []
    for i in brackets_str:
        if i is open_char:
            bracket_arr.append(i)
        elif i is close_char:
            if ((len(bracket_arr) > 0) and "[" == bracket_arr[len(bracket_arr)-1]):
                bracket_arr.pop()
            else:
                return "Unbalanced"
    if len(bracket_arr) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


def check_email_card_style(str_check):
    if (re.findall(r"(\w+)+ +(\b[A-Z]{1})", str_check)):
        return 'type Apellido N'

    if(re.findall(r"^[a-z0-9!#$%&'*ç+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", str_check)):
        return 'email'

    str_card_number = str_check.replace('-', '')
    str_card_number = str_card_number.replace(' ', '')
    if(re.findall(r"[0-9]{16}", str_card_number)):
        return 'card number'

    return 'not indentified'


def generateRectangle():
    background_colors = ','.join(
        [str(randrange(256)), str(randrange(256)), str(randrange(256))])
    border_colors = ','.join(
        [str(randrange(256)), str(randrange(256)), str(randrange(256))])
    positionX = str(randrange(360))
    positionY = str(randrange(360))
    positionZ = str(randrange(360))
    height = str(randrange(500))
    width = str(randrange(500))
    svg_data = f'<svg transform="rotate({positionX} {positionY},{positionZ})" width=\"{height}\" height=\"{width}\"><rect width=\"{height}\" height=\"{width}\" style=\"fill:rgb({background_colors});stroke-width:5;stroke:rgb({border_colors})\" /></svg>'
    return svg_data


def generatCircle():
    background_colors = ','.join(
        [str(randrange(256)), str(randrange(256)), str(randrange(256))])
    border_colors = ','.join(
        [str(randrange(256)), str(randrange(256)), str(randrange(256))])
    height = str(randrange(500))
    width = str(randrange(500))
    cx = str(randrange(200))
    cy = str(randrange(200))
    rx = str(randrange(200))
    ry = str(randrange(200))
    svg_data = f'<svg height = "{height}" width = "{width}" ><ellipse cx = "{cx}" cy = "{cy}" rx = "{rx}" ry = "{ry}" style = "fill:rgb({background_colors});stroke:rgb({border_colors});stroke-width:2" /></svg>'
    return svg_data


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
