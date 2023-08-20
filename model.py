import json


class Note:


    def __init__(self, path: str = 'Notes.json'):
        self._record: list[dict[str, str]] = []
        self._path = path
        self._last_id = 0


    def open(self):
        with open(self._path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
            # data = json.load(file)
        for notes in data:
            notes = notes.strip().split(';')
            new_dict = {'id': notes[0], 'name': notes[1], 'body': notes[2], 'date': notes[3]}
            self._record.append(new_dict)


    def save(self):
        data = []
        for notes in self._record:
            data.append(';'.join([value for value in notes.values()]))
        data = '\n'.join(data)
        with open(self._path, 'w', encoding='UTF-8') as file:
            # json.dump(data, file)
            file.write(json.dumps(data))

    def load(self):
        return self._record


    def add(self, new: dict[str, str]) -> str:
        self._last_id += 1
        new['id'] = str(self._last_id)
        self._record.append(new)
        return new.get('name')


    def search(self, word: str) -> list[dict[str, str]]:
        result: list[dict[str, str]] = []
        for notes in self._record:
            for field in notes.values():
                if word.lower() in field.lower():
                    result.append(notes)
                    break
        return result


    def change(self, new: dict, index: int | str) -> str:
        for notes in self._record:
            if index == notes.get('id'):
                notes['name'] = new.get('name', notes.get('name'))
                notes['body'] = new.get('body', notes.get('body'))
                notes['date'] = new.get('date', notes.get('date'))
                return notes.get('name')

    #
    # def show(self):
    #     print('\n' + '=' * 71)
    #     for notes in self._record:
    #         print(
    #             f'{notes.get("id"):>3}. {notes.get("name"):<20} | {notes.get("body"):^20} | {notes.get("date"):<20}')
    #     print('=' * 71 + '\n')


    def delete(self, index: int | str):
        for notes in self._record:
            if index == notes.get('id'):
                # notes.pop(index, notes)
                self._record.pop(self, index)
                # dict.pop(index, notes)

    # def filter_by_data(self, new: dict, index: int | str):
    #     for notes in self._record:
    #         if index == notes.get('id'):
    #             dict.pop(index, notes)
