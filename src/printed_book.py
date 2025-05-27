from book import Book

class PrintedBook(Book):
    def __init__(self, title, author, genre, rating, pages):
        super().__init__(title, author, genre, rating)
        self.__pages = pages

    @property
    def pages(self):
        return self.__pages

    # Polimorfismo: Sobrescribimos el método describe
    def describe(self):
        base_desc = super().describe()
        return f"{base_desc} [Printed Book, {self.pages} pages]"
