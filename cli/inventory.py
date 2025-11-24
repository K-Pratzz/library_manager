from pathlib import Path
import json
import logging
from book import Book

logging.basicConfig(level=logging.INFO)

class Inventory:
    def _init_(self):
        self.file_path = Path("books.json")

        if not self.file_path.exists():
            self.file_path.write_text("[]")

    def load_books(self):
        data = json.loads(self.file_path.read_text())
        return [Book(**item) for item in data]

    def save_books(self, books):
        data = [b.to_dict() for b in books]
        self.file_path.write_text(json.dumps(data, indent=2))

    def add_book(self, title, author):
        books = self.load_books()
        books.append(Book(title, author))
        self.save_books(books)
        logging.info("Book added.")

    def view_books(self):
        return self.load_books()