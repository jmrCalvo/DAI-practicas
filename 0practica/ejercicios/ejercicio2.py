from random import randrange
import time

ARR_SIZE = 1000
ARR_RANGE_RAMDOM_SIZE = 1000


def generateArray():
    arr_size = randrange(ARR_SIZE)
    array = []
    for i in range(0, arr_size):
        array.append(randrange(ARR_RANGE_RAMDOM_SIZE))
    return array


def burbuja_sort(array):
    array_copy = array.copy()
    for nTimes in range(len(array_copy)-1, 0, -1):
        for i in range(nTimes):
            if array_copy[i] > array_copy[i+1]:
                temp = array_copy[i]
                array_copy[i] = array_copy[i+1]
                array_copy[i+1] = temp
    return array_copy


def seleccion_sort(array):
    array_copy = array.copy()
    for i in range(len(array_copy)):
        min_idx = i
        for j in range(i+1, len(array_copy)):
            if array_copy[min_idx] > array_copy[j]:
                min_idx = j
        array_copy[i], array_copy[min_idx] = array_copy[min_idx], array_copy[i]
    return array_copy


def insercion_sort(array):
    array_copy = array.copy()
    for i in range(1, len(array_copy)):
        key = array_copy[i]
        j = i-1
        while j >= 0 and key < array_copy[j]:
            array_copy[j+1] = array_copy[j]
            j -= 1
        array_copy[j+1] = key
    return array_copy


if __name__ == "__main__":
    arr = generateArray()
    # print(arr)
    start_time_burbuja = time.time()
    burbuja_arr = burbuja_sort(arr)
    print("%ss Burbuja" % (time.time() - start_time_burbuja))

    start_time_seleccion = time.time()
    seleccion_arr = seleccion_sort(arr)
    print("%ss Seleccion" % (time.time() - start_time_seleccion))

    start_time_inserccion = time.time()
    inserccion_arr = insercion_sort(arr)
    print("%ss Inserccion" % (time.time() - start_time_inserccion))
