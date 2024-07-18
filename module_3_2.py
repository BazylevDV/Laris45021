def send_email(message, recipient, *,
               sender="university.help@gmail.com"):  # Проверка на корректность e-mail отправителя и получателя

    if "@" not in sender or not sender.endswith((".com", ".ru", ".net", ".COM", ".RU", ".NET")) or \
            "@" not in recipient or not recipient.endswith((".com", ".ru", ".net", ".COM", ".RU", ".NET")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return

    if sender == recipient:  # Проверка на отправку самому себе
        print("Нельзя отправить письмо самому себе!")
        return

    if sender == "university.help@gmail.com":  # Проверка на отправителя по умолчанию
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')