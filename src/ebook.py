from book import Book

class Ebook(Book):
    def __init__(self, title, author, genre, rating, file_size_mb):
        super().__init__(title, author, genre, rating)
        self.__file_size_mb = file_size_mb

    @property
    def file_size_mb(self):
        return self.__file_size_mb

    # Polimorfismo: Sobrescribimos el método describe
    def describe(self):
        base_desc = super().describe()
        return f"{base_desc} [Ebook, {self.file_size_mb} MB]"
