import text

def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)

def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')


def print_note(book: list[dict[str, str]], error: str):
    if book:
        print('\n' + '=' * 71)
        for notes in book:
            print(f'{notes.get("id"):>3}. {notes.get("name"):<20} | {notes.get("body"):^20} | {notes.get("date"):<20}')
        print('=' * 71 + '\n')
    else:
        print_message(error)


def input_note(message) -> dict[str, str]:
    new = {}
    print(message)
    for key, txt in text.new_note.items():
        value = input(txt)
        if value:
            new[key] = value
    return new

def input_search(message) -> str:
    return input(message)


