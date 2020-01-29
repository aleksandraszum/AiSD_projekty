def my_bubblesort(array):
    while True:
        conditions = False
        for i in range(len(array) - 1):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                conditions = True
        print(conditions)
        if conditions == False:
            break
    return array


array = [6, 0, 13, 11, 3, 8, 4, 2, 15, 12, 1, 10, 9, 5, 7]
print(my_bubblesort(array))
