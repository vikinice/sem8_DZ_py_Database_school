def get_user_data():
    return f"\n{input('Введите фамилию: ')} {input('Введите имя: ')} {input('Введите класс: ')[:].upper()}"

def menu():
    return input('\n             ВЫБЕРИТЕ НОМЕР КАТЕГОРИИ:\n \
                1 - показать все фамилии\n \
                2 - показать все имена\n \
                3 - показать все № классов\n \
                4 - показать учеников выбранного класса\n \
                5 - показать всю таблицу\n \
                6 - показать информацию по ученику\n \
                7 - добавить ученика\n \
                8 - выход\n')    