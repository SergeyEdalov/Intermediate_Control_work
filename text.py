main_menu = '''\nГлавное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать все записи
    4. Добавить запись
    5. Найти запись
    6. Изменить запись
    7. Удалить запись
    8. Выход\n'''

input_choice = 'Выберите пункт меню: '

load_successful = 'Заметки успешно открыты!'
save_successful = 'Заметки успешно сохранены!'

note_empty = 'Заметки пусты или не загружены!'

input_new_note = 'Введите данные новой заметки: '
new_note = {'name': 'Введите имя: ',
               'body': 'Введите тело заметки: ',
               'date': 'Введите дату: '}

def new_note_successful(name: str):
    return f'Заметка {name} успешно добавлена'

input_search = 'Что будем искать: '

def empty_search(word) -> str:
    return f'Заметки, содержащие слово "{word}" не найдены'

input_change = 'Какую заметку будем менять: '
input_index = 'Введите индекс заметки: '

change_note = 'Введите новые данные или оставьте поле пустым, чтоб не менять: '

def change_successful(name: str) -> str:
    return f'Заметка {name} успешно изменена!'

def delete_successful(name: str) -> str:
    return f'Заметка {name} успешно удалена!'