import read_base
import change_base
import find_data
from log import *

print ('Введите значение для выбора:\n\
1 - Просмотр базы данных\n\
2 - Добавить запись\n\
3 - Удалить запись\n\
4 - Изменить запись\n')
try:
    type_menu = int(input())
    logger.debug(f'create_base.py/ Введенное значение - {type_menu}')
    if type_menu == 1:
        read_base.read_data()
    elif type_menu == 2:
        change_base.create_card()
    elif type_menu == 3:
        change_base.delete_card()
    elif type_menu == 4:
        change_base.change.card()
    elif type_menu == 5:
        find_data.find_p()
    else:
        print('Неверный ввод')
        logger.debug(f'create_base.py / "Неверный ввод"')
except ValueError:
    print('Неверный формат ввода')
    logger.debug(f'create_base.py / ValueError')