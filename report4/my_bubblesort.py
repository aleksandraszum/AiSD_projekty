def my_bubblesort(array, sort_type):
    """
    function returns sorted list by bubble method
        :param array:
        :param sort_type: 'ASC' - ascending sorting, 'DSC" - descending sorting
    :return:
        array - sorted list
        computational_complexity
    """
    computational_complexity = 0
    while True:
        conditions = False
        computational_complexity = computational_complexity + 1
        for i in range(len(array) - 1):
            computational_complexity = computational_complexity + 1
            if sort_type == 'ASC':
                if (array[i] > array[i + 1]):
                    array[i], array[i + 1] = array[i + 1], array[i]
                    conditions = True
            else:
                if (array[i] < array[i + 1]):
                    array[i], array[i + 1] = array[i + 1], array[i]
                    conditions = True
        if conditions == False:
            break
    return array, computational_complexity


array = [6, 0, 13, 11, 3, 8, 4, 2, 15, 12, 1, 10, 9, 5, 7]
print('My array:', array)
sorted_array, complex1 = my_bubblesort(array, 'ASC')
print('My sorted array:', sorted_array)
print('Computational complexity', complex1)
sorted_array_ASC, complex2 = my_bubblesort(sorted_array, 'ASC')
print('My sorted array:', sorted_array_ASC)
print('Computational complexity', complex2)
sorted_array_DSC, complex3 = my_bubblesort(sorted_array_ASC, 'DSC')
print('My sorted array by DSC:', sorted_array_DSC)
print('Computational complexity', complex3)

n = len(array)
print('O(n^2) = ', n ** 2)
