from collections import UserDict
from datetime import datetime

class Note:
    def __init__(self, title, content):
        self.title = title  # Назва нотатки, що служить ключем
        self.content = content  # Текст нотатки
        self.tags = set()  # Множина тегів
        self.created_at = datetime.now()  # Дата створення

    def add_tag(self, tag):
        """Додає новий тег до нотатки."""
        self.tags.add(tag)

    def remove_tag(self, tag):
        """Видаляє тег з нотатки, якщо він існує."""
        if tag in self.tags:
            self.tags.remove(tag)

    def __str__(self):
        tags = ', '.join(self.tags) if self.tags else "No tags"
        return f"Title: {self.title}\nContent: {self.content}\nTags: {tags}\nCreated at: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"


class NotesBook(UserDict):
    def __init__(self):
        super().__init__()  # Ініціалізуємо словник даних UserDict

    def add_note(self, title, content):
        """Додає нову нотатку за її назвою."""
        if title in self.data:
            return "A note with this title already exists."
        
        note = Note(title, content)
        self.data[title] = note  # Зберігаємо нотатку у словнику UserDict
        return "Note added."

    def edit_note_content(self, title, new_content):
        """Редагує текст нотатки за її назвою."""
        if title in self.data:
            self.data[title].content = new_content
            return "Note content updated."
        return "Note not found."

    def delete_note(self, title):
        """Видаляє нотатку за її назвою."""
        if title in self.data:
            del self.data[title]
            return "Note deleted."
        return "Note not found."

    def add_tag_to_note(self, title, tag):
        """Додає тег до нотатки за назвою."""
        if title in self.data:
            self.data[title].add_tag(tag)
            return "Tag added to note."
        return "Note not found."

    def remove_tag_from_note(self, title, tag):
        """Видаляє тег з нотатки за назвою."""
        if title in self.data:
            self.data[title].remove_tag(tag)
            return "Tag removed from note."
        return "Note not found."

    def search_notes_by_tag(self, tag):
        """Шукає всі нотатки, що містять заданий тег."""
        return [note for note in self.data.values() if tag in note.tags]

    
