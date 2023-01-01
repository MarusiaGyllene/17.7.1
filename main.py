array = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
number = int(input("Введите любое целое число: "))


def sorted_array(array):
    for i in range(len(array)):  # проходим по всему массиву
        idx_min = i  # сохраняем индекс предположительно минимального элемента
        for j in range(i, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j
        if i != idx_min:  # если индекс не совпадает с минимальным, меняем
            array[i], array[idx_min] = array[idx_min], array[i]
    return array #Возвращаем отсортированный массив

def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return "не найдено"  # значит элемент отсутствует
    middle = (right + left) // 2  # находимо середину
    if array[middle] < element and middle >= len(array) - 1:
        return "не найдено"  # число не найдено
    elif array[middle] < element and middle < len(array) - 1 and array[middle + 1] >= element:
        return middle  # индекс числа найден
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

print("Отсортированный массив: ", sorted_array(array))
print("Номер позиции элемента, который меньше введенного пользователем числа: ", binary_search(array, number, 0, len(array)))
