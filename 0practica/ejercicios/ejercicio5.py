from random import randrange
import math

ARR_SIZE = 100


def generate_array():
    arr_size = randrange(ARR_SIZE)
    array = []
    for i in range(0, arr_size):
      # if 0 => ]
      # else [
        brackets_random = randrange(2)
        if(brackets_random == 1):
            array.append(']')
        else:
            array.append('[')
    return array


# def check_brackets(arr):
#     if(len(arr) == 1):
#         return True
#     for i in range(math.floor((len(arr)/2)+1)):
#         print(i, len(arr) - 1 - i)
#         if(arr[i] == arr[len(arr) - 1 - i]):
#             return False
#     # print(arr, len(arr))
#     return True


def check(brackets_str):
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


if __name__ == "__main__":
    bracket_arr = "".join(generate_array())
    print(bracket_arr)
    print(check(bracket_arr))
