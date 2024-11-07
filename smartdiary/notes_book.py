from datetime import datetime
from collections import UserDict

class Note:
    def __init__(self, content, tags=None):
        self.content = content  # Текст нотатки
        self.tags = set(tags) if tags else set()  # Множина тегів для унікальності
        self.created_at = datetime.now()  # Дата створення

    def add_tag(self, tag):
        """Додає тег до нотатки."""
        self.tags.add(tag)

    def remove_tag(self, tag):
        """Видаляє тег з нотатки, якщо він існує."""
        if tag in self.tags:
            self.tags.remove(tag)

    def __str__(self):
        """Відображає нотатку з її тегами."""
        tags = ', '.join(self.tags)
        return f"{self.content} | Tags: {tags}"

    def contains_keyword(self, keyword):
        """Перевіряє, чи містить вміст нотатки ключове слово (незалежно від регістру)."""
        return keyword.lower() in self.content.lower()

    def has_tag(self, tag):
        """Перевіряє, чи має нотатка вказаний тег."""
        return tag in self.tags


class NotesBook:
    def __init__(self):
        self.notes = []  # Список нотаток

    def add_note(self, content, tags=None):
        """Додає нову нотатку з вказаними тегами."""
        note = Note(content, tags)
        self.notes.append(note)
        return "Note added."

    def edit_note(self, index, new_content):
        """Редагує нотатку за індексом."""
        if 0 <= index < len(self.notes):
            self.notes[index].content = new_content
            return "Note updated."
        return "Note not found."

    def delete_note(self, index):
        """Видаляє нотатку за індексом."""
        if 0 <= index < len(self.notes):
            del self.notes[index]
            return "Note deleted."
        return "Note not found."

    def search_notes_by_keyword(self, keyword):
        """Повертає всі нотатки, що містять ключове слово."""
        return [note for note in self.notes if note.contains_keyword(keyword)]

    def search_notes_by_tag(self, tag):
        """Повертає всі нотатки, що містять вказаний тег."""
        return [note for note in self.notes if note.has_tag(tag)]

    def sort_notes_by_tag(self, tag):
        """Сортує нотатки за наявністю вказаного тегу, розміщуючи нотатки з цим тегом першими."""
        return sorted(self.notes, key=lambda note: tag in note.tags, reverse=True)

    def show_all_notes(self):
        """Відображає всі нотатки з їхніми тегами."""
        return "\n".join(str(note) for note in self.notes)
