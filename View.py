import Controller


def main_menu():
    while True:
        print('\nГлавное меню:')
        print('0. Открыть файл с заметками')
        print('1. Добавить заметку')
        print('2. Удалить заметку')
        print('3. Редактировать заметку')
        print('9. Закрыть программу')
        select = int(input('Выберите пункт: '))
        match select:
            case 0:
                Controller.read_all_notes()
            case 1:
                Controller.add_note()
            case 2:
                Controller.delete_note()
            case 3:
                Controller.edit_note()
            case 9:
                exit()
