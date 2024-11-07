from datetime import datetime
from collections import UserDict

from datetime import datetime

class Note:
    def __init__(self, content):
        self.content = content  # Текст нотатки
        self.tags = set()  # Порожня множина для тегів
        self.created_at = datetime.now()  # Дата створення

    def add_tag(self, tag):
        """Додає новий тег до нотатки."""
        self.tags.add(tag)

    def remove_tag(self, tag):
        """Видаляє тег з нотатки, якщо він існує."""
        if tag in self.tags:
            self.tags.remove(tag)

    def __str__(self):
        tags = ', '.join(self.tags)
        return f"{self.content} | Tags: {tags}"


class NotesBook:
    def __init__(self):
        self.notes = []  # Список нотаток

    def add_note(self, content):
        """Додає нову нотатку без тегів."""
        note = Note(content)
        self.notes.append(note)
        return "Note added."

    def add_tag_to_note(self, index, tag):
        """Додає тег до існуючої нотатки за індексом."""
        if 0 <= index < len(self.notes):
            self.notes[index].add_tag(tag)
            return "Tag added to note."
        return "Note not found."

    def remove_tag_from_note(self, index, tag):
        """Видаляє тег з існуючої нотатки за індексом."""
        if 0 <= index < len(self.notes):
            self.notes[index].remove_tag(tag)
            return "Tag removed from note."
        return "Note not found."

    def show_all_notes(self):
        """Відображає всі нотатки з їхніми тегами."""
        return "\n".join(str(note) for note in self.notes)
