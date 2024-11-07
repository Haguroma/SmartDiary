

import uuid
from collections import UserDict
from datetime import datetime

class Note:
    def __init__(self, content):
        self.id = str(uuid.uuid4())  # Автоматично генерується унікальний ідентифікатор
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
        return f"ID: {self.id}\nContent: {self.content}\nTags: {tags}\nCreated at: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"


class NotesBook(UserDict):
    def add_note(self, content):
        """Додає нову нотатку з автоматичним унікальним ідентифікатором."""
        note = Note(content)
        self.data[note.id] = note  # Використовуємо автоматично згенерований id як ключ
        return f"Note added with ID: {note.id}"

    def edit_note_content(self, note_id, new_content):
        """Редагує текст нотатки за її унікальним ідентифікатором."""
        if note_id in self.data:
            self.data[note_id].content = new_content
            return "Note content updated."
        return "Note not found."

    def delete_note(self, note_id):
        """Видаляє нотатку за її унікальним ідентифікатором."""
        if note_id in self.data:
            del self.data[note_id]
            return "Note deleted."
        return "Note not found."

    def add_tag_to_note(self, note_id, tag):
        """Додає тег до нотатки за унікальним ідентифікатором."""
        if note_id in self.data:
            self.data[note_id].add_tag(tag)
            return "Tag added to note."
        return "Note not found."

    def remove_tag_from_note(self, note_id, tag):
        """Видаляє тег з нотатки за унікальним ідентифікатором."""
        if note_id in self.data:
            self.data[note_id].remove_tag(tag)
            return "Tag removed from note."
        return "Note not found."

    def search_notes_by_tag(self, tag):
        """Шукає всі нотатки, що містять заданий тег."""
        return [note for note in self.data.values() if tag in note.tags]

    def show_all_notes(self):
        """Відображає всі нотатки з їхніми тегами."""
        if not self.data:
            return "No notes available."
        
        return "\n\n".join(str(note) for note in self.data.values())


    
