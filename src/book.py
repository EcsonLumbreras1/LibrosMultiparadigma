class Book:
    def __init__(self, title, author, genre, rating):
        self.__title = title         # atributo privado
        self.__author = author
        self.__genre = genre
        self.__rating = rating

    # Métodos getter para acceder a los atributos
    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def genre(self):
        return self.__genre

    @property
    def rating(self):
        return self.__rating

    def describe(self):
        return f"'{self.title}' by {self.author} - Genre: {self.genre}, Rating: {self.rating}"

    def __str__(self):
        return self.describe()
