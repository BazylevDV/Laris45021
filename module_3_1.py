calls = 0  # Функция для подсчета вызовов


def count_calls():
    global calls
    calls += 1


def string_info(string):  # Функция для получения информации о строке
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string, list_to_search):  # Функция для проверки наличия строки в списке
    count_calls()
    string_lower = string.lower()
    for item in list_to_search:
        if string_lower == item.lower():
            return True
    return False


print(string_info('Capybara'))  # Пример выполнения функций
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)  # Вывод количества вызовов функций
