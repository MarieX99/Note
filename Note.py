import json
import datetime


class Note:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.date = datetime.datetime.now()

    def to_json(self):
        return json.dumps({

        'id': self.id,
        'title': self.title,
        'body': self.body,
        'date': self.date.strftime('%d-%m-%Y %H:%M:%S')
        })
class NotesManager:
    
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.notes = []    
    def load_notes(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        self.notes = [
            Note(  
                note['id'],
                note['title'],
                note['body']
            )   
            for note in data
        ]  
                        
    def save_notes(self):  
        with open(self.file_path, 'w') as file:
            json.dump([note.to_json() for note in self.notes], file)
    
    def add_note(self, note):
        self.notes.append(note)
    
    def edit_note(self, id, new_title, new_body):
        for note in self.notes:
            if note.id == id:  
                note.title = new_title
                note.body = new_body
                note.date = datetime.datetime.now()
                break

    def  delete_note(self, id):
        self.notes = [note for note in self.notes if note.id != id]
    
    def filter_notes_by_date(self, date):
        return [note for note in self.notes if note.date.date() == date.date()]  

def add_note():
    manager = NotesManager('notes.json')
    # manager.load_notes()  
    id = input('Введите ID-номер заметки: ')
    title = input('Введите название заметки: ')
    body = input('Введите текст заметки: ') 
    note = Note(id, title, body)
    manager.add_note(note)
    manager.save_notes()
    print('Заметка сохранена')

def edit_note():
        manager = NotesManager('notes.json')
        # manager.load_notes()  
        id = input('Введите ID номер заметки для редактирования: ')
        new_title = input('Новый заголовок: ')
        new_body = input('Текст заметки: ') 
        manager.edit_note(id, new_title, new_body)
        manager.save_notes()
        print('Заметка отредактирована')

def delete_note():
        manager = NotesManager('notes.json')
        # manager.load_notes()  
        id = input('Введите id-номер заметки для удаления: ')
        manager.delete_note(id)
        manager.save_notes()
        print('Заметка удалена')

def filter_notes_by_date():
    manager = NotesManager('notes.json')
    # manager.load_notes()  
    date = input('Введите дату заметки (ДД-ММ-ГГГГ): ')
    try:
        date = datetime.datetime.strptime(date, '%d-%m-%Y').date()
        filtered_notes = manager.filter_notes_by_date(date)
        if filtered_notes:
            print(f'Найдены заметки за период {date}: ')
            for note in filtered_notes:
                print(f'ID: {note.id}, Заголовок: {note.title}')
            else:
                print(f'Заметок за период {date} не найдено') 
    except ValueError:
            print('Неверно заданный формат даты')
def main():
        manager = NotesManager('notes.json')
        manager.load_notes()    
while True:
        print('1. Создать новую заметку')
        print('2. Редактировать заметку')
        print('3. Удалить заметку')
        print('4. Отфильровать заметки')
        print('5. Выход')
            
        choice = input('Выбирите действие: ')
            
        if choice == '1':
            add_note()
        elif choice == '2':
            edit_note()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            filter_notes_by_date()
        elif choice == '5':
            break    
        else:
            print('Неправильный выбор. попробуйте еще раз')      
if __name__ == '__main__':
    main()