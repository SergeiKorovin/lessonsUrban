def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i_numbers in numbers:
        try:
            result += i_numbers
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {i_numbers}')
            incorrect_data += 1
    return (result, incorrect_data)

def calculate_average(numbers):
    try:
        count = 0
        for i_number in numbers:
            if isinstance(i_number, int):
                count += 1
        average = personal_sum(numbers)[0] / count
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
    else:
        return average

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
