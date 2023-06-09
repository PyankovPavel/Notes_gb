import json
import datetime
import Model
import View


def start_app():
    View.main_menu()


def save_notes(notes):
    with open(Model.file_path, "w") as f:
        json.dump(notes, f)


def load_notes():
    try:
        with open(Model.file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def add_note():
    title = input('Введите название заметки: ')
    message = input('Введите текст заметки: ')
    notes = load_notes()
    if not notes:
        id = 1
    else:
        id = notes[-1]["id"] + 1
    date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    note = {"id": id, "title": title, "message": message, "date": date}
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно добавлена.")


def edit_note():
    notes = load_notes()
    id = int(input('Введите id заметки: '))
    for note in notes:
        if note["id"] == id:
            print('Будет изменена данная заметка: {}'.format(notes[id - 1]))
            title = input('Введите новое название заметки: ')
            message = input('Введите новый текст заметки: ')
            if title:
                note["title"] = title
            if message:
                note["message"] = message
            note["date"] = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно изменена.")
            break
    else:
        print("Заметка не найдена.")


def delete_note():
    notes = load_notes()
    id = int(input('Введите id заметки: '))
    for i, note in enumerate(notes):
        if note["id"] == id:
            print('Будет удалена данная заметка: {}'.format(notes[id - 1]))
            del notes[i]
            save_notes(notes)
            print("Заметка успешно удалена.")
            break
    else:
        print("Заметка не найдена.")


def read_all_notes(date=None):
    notes = load_notes()
    if date:
        notes = [note for note in notes if note["date"].startswith(date)]
    for note in notes:
        print(f"#{note['id']} {note['title']}\n{note['message']}\nДата создания: {note['date']}\n")
