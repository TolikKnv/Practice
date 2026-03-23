class LibraryItem:
    def __init__(self, title, item_id, pages):
        self.title = title
        self.item_id = item_id
        self.pages = pages

    def __str__(self):
        return f"{self.title} (ID: {self.item_id}), страниц: {self.pages}"

    def __eq__(self, other):
        if isinstance(other, LibraryItem) == False:
            return 'NotImplemented'
        if self.pages == other.pages:
            return True
        return False


class Book(LibraryItem):
    def __init__(self, title, item_id, pages, author):
        super().__init__(title, item_id, pages)
        self.author = author

    def __str__(self):
        return f"{super().__str__()} (автор: {self.author})"


book1 = Book('Война и мир', 'B001', 1200, 'Л. Толстой')
print(book1)
book2 = Book('Анна Каренина', 'B002', 800, 'Л. Толстой')
print(book2)
3