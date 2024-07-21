def single_root_words(root_word, *other_words):
    root_word_lower = root_word.lower()  # Приводим root_word к нижнему регистру
    same_words = []  # Создаем пустой список для хранения подходящих слов

    for word in other_words:  # Перебираем все слова в other_words
        word_lower = word.lower()  # Приводим текущее слово к нижнему регистру
        if root_word_lower in word_lower or word_lower in root_word_lower:  # Проверяем, содержится ли root_word в текущем слове или текущее слово в root_word
            same_words.append(word)  # Если условие выполняется, добавляем слово в список same_words

    return same_words  # Возвращаем список same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')# Примеры вызова функции и вывода результатов
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)