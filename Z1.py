def merge_sorted_lists_descending(list1, list2):
    # Инициализируем переменные для итерации по двум спискам
    i = 0  # Индекс для списка list1
    j = 0  # Индекс для списка list2
    res = []  # Результирующий список

    # Продолжаем добавлять элементы до тех пор, пока не пройдем оба списка полностью
    while i < len(list1) and j < len(list2):
        if list1[i] >= list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1

    # Добавляем оставшиеся элементы из list1, если таковые есть
    while i < len(list1):
        res.append(list1[i])
        i += 1

    # Добавляем оставшиеся элементы из list2, если таковые есть
    while j < len(list2):
        res.append(list2[j])
        j += 1

    # Результирующий список res теперь содержит объединенные и отсортированные элементы по убыванию
    return res


# Пример использования
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]

sorted_list_desc = merge_sorted_lists_descending(list1, list2)
print(sorted_list_desc)

