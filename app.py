'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''


def searchMatrix(matrix: list, target: int) -> bool:
    # Проверяем, что матрица не пустая
    if not matrix:
        return False
    # Получаем количество строк и столбцов в матрице
    m = len(matrix)
    n = len(matrix[0])
    # Устанавливаем левую и правую границы матрицы, преобразуя индексы её крайних элементов в одномерный массив
    left  = 0
    right = m * n - 1
    # Используем алгоритм бинарного поиска
    while left <= right:
        # Находим середину матрицы (как одномерного массива)
        mid = (left + right) // 2
        # Находим значение в середине матрицы , преобразуя данные из одномерного массива обратно в нормальный вид матрицы (list[строка][столбец])
        # mid // n, индекс через деление без остатка. mid % n остаток от деления в одномерном массиве равен индексу столбца в матрице
        mid_val = matrix[mid // n][mid % n]
        # Если значение в середине равно целевому числу, возвращаем True
        if mid_val == target:
            return True
        # Если значение в середине меньше целевого числа, ищем в верхней половине матрицы
        elif mid_val < target:
            left = mid + 1
        # Если значение в середине больше целевого числа, ищем в нижней половине матрицы
        else:
            right = mid - 1
    # Если целевое число не найдено, возвращаем False
    return False

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
    target = 11
    print('Проверка наличия числа: ',searchMatrix(matrix,target))
